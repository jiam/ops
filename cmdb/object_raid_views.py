# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import RAID 
import json
import urllib
import cmdb_log

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def raid_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        raid_r = list(RAID.objects.all().values())
        data = {"total":len(raid_r),"data":raid_r[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        raid_r = list(RAID.objects.filter(id=id).values())[0]
        json_r = json.dumps(raid_r)
    else:
        raid_r = list(RAID.objects.filter(RAID_Type__contains=key).values())
        json_r = json.dumps(raid_r)
    return HttpResponse(json_r)

@csrf_exempt
def raid_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        raid_r = list(RAID.objects.filter(id=data['id']).values())[0]
        json_r = json.dumps(raid_r)
    if key == 'RAID_Type':
        raid_r = list(RAID.objects.filter(RAID_Type__contains=data['RAID_Type']).values())[0]
        json_r = json.dumps(raid_r)
    return HttpResponse(json_r)

@csrf_exempt  
def raid_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_raid'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        i = RAID.objects.filter(id=data['id'])
        message = cmdb_log.cmp(list(i.values())[0],data)
        i.update(RAID_Cache = data['RAID_Cache'],RAID_Type = data['RAID_Type'],RAID_Battery = data['RAID_Battery'])
        cmdb_log.log_change(request,i[0],data['RAID_Type'],message)
    else:
        i = RAID(RAID_Cache = data['RAID_Cache'],RAID_Type = data['RAID_Type'],RAID_Battery = data['RAID_Battery'])
        i.save()
        cmdb_log.log_addition(request,i,data['RAID_Type'],data)
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(json_r)
@csrf_exempt
def raid_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_raid'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id'].split(',')
    for del_id in ids:
        i = RAID.objects.filter(id=del_id)
        cmdb_log.log_deletion(request,i[0],i[0].RAID_Type,data)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)
