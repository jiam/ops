# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import Zone 
from cmdb.models import IDC
import json
import urllib
import cmdb_log

from django.views.decorators.csrf import csrf_exempt

def zone_get_byid(request,id):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    id = id
    zones = list(Zone.objects.filter(idc=id).values())
    json_r = json.dumps(zones)
    return HttpResponse(json_r)
    
@csrf_exempt  
def zone_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    zone_list = []
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        zones = Zone.objects.select_related().all()
        for zone in zones:
            zone_d = {'IDC_id':zone.idc.IDC_Name,'Zone_Name':zone.Zone_Name,'id':zone.id}            
            zone_list.append(zone_d)
        data = {"total":len(zone_list),"data":zone_list[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        zone = Zone.objects.get(id=id)
        zone_d = {'IDC_id':zone.idc.id,'Zone_Name':zone.Zone_Name,'id':zone.id}
        json_r = json.dumps(zone_d)
    else:
        zones= Zone.objects.filter(Zone_Name__contains=key)
        for zone in zones:
            zone_d = {'IDC_id':zone.idc.IDC_Name,'Zone_Name':zone.Zone_Name,'id':zone.id}            
            zone_list.append(zone_d)
        #data = {"total":len(zone_list),"data":zone_list}
        json_r = json.dumps(zone_list)
    return HttpResponse(json_r)

@csrf_exempt
def zone_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("http://cmdb.ops.creditease.corp/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        zone = Zone.objects.get(id=data['id'])
        zone_d = {'IDC_id':zone.idc.id,'Zone_Name':zone.Zone_Name,'id':zone.id}
        json_r = json.dumps(zone_d)
    if key == 'Zone_Name':
        zone_r = list(Zone.objects.filter(Zone_Name__contains=data['Zone_Name']).values())[0]
        json_r = json.dumps(zone_r)
    return HttpResponse(json_r)

@csrf_exempt  
def zone_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_zone'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        r = Zone.objects.filter(id=data['id'])
        message = cmdb_log.cmp(list(r.values())[0],data)
        r.update(Zone_Name = data['Zone_Name'],idc = data['IDC_id'])
        cmdb_log.log_change(request,r[0],data['Zone_Name'],message)
    else:
        i = IDC.objects.get(id=data['IDC_id'])
        r = Zone(Zone_Name = data['Zone_Name'],idc = i)
        r.save()
        cmdb_log.log_addition(request,r,data['Zone_Name'],data)
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(json_r)
@csrf_exempt
def zone_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_zone'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id']
    for del_id in ids:
        i = Zone.objects.filter(id=del_id)
        cmdb_log.log_deletion(request,i[0],i[0].Zone_Name,data)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)
