# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import PCIE 
import json
import urllib
import cmdb_log

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def pcie_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        pcie_r = list(PCIE.objects.all().values())
        data = {"total":len(pcie_r),"data":pcie_r[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        pcie_r = list(PCIE.objects.filter(id=id).values())[0]
        json_r = json.dumps(pcie_r)
    else:
        pcie_r = list(PCIE.objects.filter(PCIE_Type__contains=key).values())
        json_r = json.dumps(pcie_r)
    return HttpResponse(json_r)

@csrf_exempt
def pcie_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        pcie_r = list(PCIE.objects.filter(id=data['id']).values())[0]
        json_r = json.dumps(pcie_r)
    if key == 'PCIE_Type':
        pcie_r = list(PCIE.objects.filter(PCIE_Type__contains=data['PCIE_Type']).values())[0]
        json_r = json.dumps(pcie_r)
    return HttpResponse(json_r)

@csrf_exempt  
def pcie_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_pcie'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        i = PCIE.objects.filter(id=data['id'])
        message = cmdb_log.cmp(list(i.values())[0],data)
        i.update(PCIE_Type = data['PCIE_Type'])
        cmdb_log.log_change(request,i[0],data['PCIE_Type'],message)
    else:
        i = PCIE(PCIE_Type = data['PCIE_Type'])
        i.save()
        cmdb_log.log_addition(request,i,data['PCIE_Type'],data)
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(json_r)

@csrf_exempt
def pcie_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_pcie'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id'].split(',')
    for del_id in ids:
        i = PCIE.objects.filter(id=del_id)
        cmdb_log.log_deletion(request,i[0],i[0].PCIE_Type,data)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)
