# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import OS
import json
import urllib
import cmdb_log

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def os_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        os_r = list(OS.objects.all().values())
        data = {"total":len(os_r),"data":os_r[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        os_r = list(OS.objects.filter(id=id).values())[0]
        json_r = json.dumps(os_r)
    else:
        os_r = list(OS.objects.filter(OS_Name__contains=key).values())
        json_r = json.dumps(os_r)
    return HttpResponse(json_r)

@csrf_exempt
def os_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("http://10.100.30.174/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        os_r = list(OS.objects.filter(id=data['id']).values())[0]
        json_r = json.dumps(os_r)
    if key == 'OS_Name':
        os_r = list(OS.objects.filter(OS_Name__contains=data['OS_Name']).values())[0]
        json_r = json.dumps(os_r)
    return HttpResponse(json_r)

@csrf_exempt  
def os_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_os'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        i = OS.objects.filter(id=data['id'])
        message = cmdb_log.cmp(list(i.values())[0],data)
        i.update(OS_Name = data['OS_Name'])
        cmdb_log.log_change(request,i[0],data['OS_Name'],message)
    else:
        i = OS(OS_Name = data['OS_Name'])
        i.save()
        cmdb_log.log_addition(request,i,data['OS_Name'],data)
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(json_r)

@csrf_exempt
def os_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_os'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id'].split(',')
    for del_id in ids:
        i = OS.objects.filter(id=del_id)
        cmdb_log.log_deletion(request,i[0],i[0].OS_Name,data)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)
