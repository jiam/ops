# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import Rack 
from cmdb.models import IDC
import json
import urllib

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def rack_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    rack_list = []
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        racks = Rack.objects.select_related().all()
        for rack in racks:
            rack_d = {'IDC_id':rack.idc.IDC_Name,'Rack_Name':rack.Rack_Name,'id':rack.id}            
            rack_list.append(rack_d)
        data = {"total":len(rack_list),"data":rack_list[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        rack = Rack.objects.get(id=id)
        rack_d = {'IDC_id':rack.idc.id,'Rack_Name':rack.Rack_Name,'id':rack.id}
        json_r = json.dumps(rack_d)
    else:
        racks= Rack.objects.filter(Rack_Name__contains=key)
        for rack in racks:
            rack_d = {'IDC_id':rack.idc.IDC_Name,'Rack_Name':rack.Rack_Name,'id':rack.id}            
            rack_list.append(rack_d)
        #data = {"total":len(rack_list),"data":rack_list}
        json_r = json.dumps(rack_list)
    return HttpResponse(json_r)

@csrf_exempt
def rack_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("http://10.100.30.174/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        rack = Rack.objects.get(id=data['id'])
        rack_d = {'IDC_id':rack.idc.id,'Rack_Name':rack.Rack_Name,'id':rack.id}
        json_r = json.dumps(rack_d)
    if key == 'Rack_Name':
        rack_r = list(Rack.objects.filter(Rack_Name__contains=data['Rack_Name']).values())[0]
        json_r = json.dumps(rack_r)
    return HttpResponse(json_r)

@csrf_exempt  
def rack_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_rack'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        r = Rack.objects.filter(id=data['id'])
        r.update(Rack_Name = data['Rack_Name'],idc = data['IDC_id'])
    else:
        i = IDC.objects.get(id=data['IDC_id'])
        r = Rack(Rack_Name = data['Rack_Name'],idc = i)
        r.save()
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(json_r)

@csrf_exempt
def rack_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_rack'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id'].split(',')
    for del_id in ids:
        i = Rack.objects.filter(id=del_id)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})    
    return HttpResponse(json_r)