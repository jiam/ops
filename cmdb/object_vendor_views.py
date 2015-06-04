# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import Vendor 
import json
import urllib
import cmdb_log

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def vendor_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        vendor_r = list(Vendor.objects.all().values())
        data = {"total":len(vendor_r),"data":vendor_r[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        vendor_r = list(Vendor.objects.filter(id=id).values())[0]
        json_r = json.dumps(vendor_r)
    else:
        vendor_r = list(Vendor.objects.filter(Vendor_Name__contains=key).values())
        json_r = json.dumps(vendor_r)
    return HttpResponse(json_r)

@csrf_exempt
def vendor_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("http://10.100.30.174/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        vendor_r = list(Vendor.objects.filter(id=data['id']).values())[0]
        json_r = json.dumps(vendor_r)
    if key == 'Vendor_Name':
        vendor_r = list(Vendor.objects.filter(Vendor_Name__contains=data['Vendor_Name']).values())[0]
        json_r = json.dumps(vendor_r)
    return HttpResponse(json_r)

@csrf_exempt  
def vendor_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_vendor'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        i = Vendor.objects.filter(id=data['id'])
        i.update(Vendor_Name = data['Vendor_Name'])
        cmdb_log.log_change(request,i[0],i[0].Vendor_Name,data)
    else:
        i = Vendor(Vendor_Name = data['Vendor_Name'])
        i.save()
        cmdb_log.log_addition(request,i,i.Vendor_Name,data)
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(json_r)

@csrf_exempt
def vendor_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_vendor'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id']
    for del_id in ids:
        i = Vendor.objects.filter(id=del_id)
        cmdb_log.log_deletion(request,i[0],i[0].Vendor_Name,data)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)
