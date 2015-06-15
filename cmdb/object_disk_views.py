# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import Disk 
import json
import urllib
import cmdb_log

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def disk_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        disk_r = list(Disk.objects.all().values())
        data = {"total":len(disk_r),"data":disk_r[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        disk_r = list(Disk.objects.filter(id=id).values())[0]
        json_r = json.dumps(disk_r)
    else:
        disk_r = list(Disk.objects.filter(Disk_Type__contains=key).values())
        json_r = json.dumps(disk_r)
    return HttpResponse(json_r)

@csrf_exempt
def disk_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        disk_r = list(Disk.objects.filter(id=data['id']).values())[0]
        json_r = json.dumps(disk_r)
    if key == 'Disk_Type':
        disk_r = list(Disk.objects.filter(Disk_Type__contains=data['Disk_Type']).values())[0]
        json_r = json.dumps(disk_r)
    return HttpResponse(json_r)

@csrf_exempt  
def disk_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_disk'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        i = Disk.objects.filter(id=data['id'])
        message = cmdb_log.cmp(list(i.values())[0],data)
        i.update(Disk_Type = data['Disk_Type'])
        cmdb_log.log_change(request,i[0],data['Disk_Type'],message)
    else:
        i = Disk(Disk_Type = data['Disk_Type'])
        i.save()
        cmdb_log.log_addition(request,i,data['Disk_Type'],data)
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(json_r)

@csrf_exempt
def disk_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_disk'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id'].split(',')
    for del_id in ids:
        i = Disk.objects.filter(id=del_id)
        cmdb_log.log_deletion(request,i[0],i[0].Disk_Type,data)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)
