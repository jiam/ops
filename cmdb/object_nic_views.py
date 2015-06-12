# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import NIC 
import json
import urllib
import cmdb_log

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def nic_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        nic_r = list(NIC.objects.all().values())
        data = {"total":len(nic_r),"data":nic_r[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        nic_r = list(NIC.objects.filter(id=id).values())[0]
        json_r = json.dumps(nic_r)
    else:
        nic_r = list(NIC.objects.filter(NIC_Type__contains=key).values())
        json_r = json.dumps(nic_r)
    return HttpResponse(json_r)

@csrf_exempt
def nic_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("http://cmdb.ops.creditease.corp/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        nic_r = list(NIC.objects.filter(id=data['id']).values())[0]
        json_r = json.dumps(nic_r)
    if key == 'NIC_Type':
        nic_r = list(NIC.objects.filter(NIC_Type__contains=data['NIC_Type']).values())[0]
        json_r = json.dumps(nic_r)
    return HttpResponse(json_r)

@csrf_exempt  
def nic_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_nic'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        i = NIC.objects.filter(id=data['id'])
        message = cmdb_log.cmp(list(i.values())[0],data)
        i.update(NIC_Type = data['NIC_Type'])
        cmdb_log.log_change(request,i[0],data['NIC_Type'],message)
    else:
        i = NIC(NIC_Type = data['NIC_Type'])
        i.save()
        cmdb_log.log_addition(request,i,data['NIC_Type'],data)
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(json_r)

@csrf_exempt
def nic_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_nic'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id'].split(',')
    for del_id in ids:
        i = NIC.objects.filter(id=del_id)
        cmdb_log.log_deletion(request,i[0],i[0].NIC_Type,data)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)
