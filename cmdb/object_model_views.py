# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import Vendor
from cmdb.models import Model
import json
import urllib
import cmdb_log

from django.views.decorators.csrf import csrf_exempt

def model_get_byid(request,id):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    id = id
    models = list(Model.objects.filter(vendor=id).values())
    json_r = json.dumps(models)
    return HttpResponse(json_r)

@csrf_exempt  
def model_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    model_list = []
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        models = Model.objects.select_related().all()
        for model in models:
            model_d = {'Vendor_id':model.vendor.Vendor_Name,'Model_Name':model.Model_Name,'id':model.id}            
            model_list.append(model_d)
        data = {"total":len(model_list),"data":model_list[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        model = Model.objects.get(id=id)
        model_d = {'Vendor_id':model.vendor.id,'Model_Name':model.Model_Name,'id':model.id}
        json_r = json.dumps(model_d)
    else:
        models= Model.objects.filter(Model_Name__contains=key)
        for model in models:
            model_d = {'vendor':model.vendor.id,'Vendor_id':model.vendor.Vendor_Name,'Model_Name':model.Model_Name,'id':model.id}            
            model_list.append(model_d)
        #data = {"total":len(model_list),"data":model_list}
        json_r = json.dumps(model_list)
    return HttpResponse(json_r)

@csrf_exempt
def model_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("http://cmdb.ops.creditease.corp/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        model = Model.objects.get(id=data['id'])
        model_d = {'Vendor_id':model.vendor.id,'Model_Name':model.Model_Name,'id':model.id}
        json_r = json.dumps(model_d)
    if key == 'Model_Name':
        model_r = list(Model.objects.filter(Model_Name__contains=data['Model_Name']).values())[0]
        json_r = json.dumps(model_r)
    return HttpResponse(json_r)

@csrf_exempt  
def model_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_model'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        r = Model.objects.filter(id=data['id'])
        message = cmdb_log.cmp(list(r.values())[0],data)
        r.update(Model_Name = data['Model_Name'],vendor = data['Vendor_id'])
        cmdb_log.log_change(request,r[0],data['Model_Name'],message)
    else:
        i = Vendor.objects.get(id=data['Vendor_id'])
        r = Model(Model_Name = data['Model_Name'],vendor = i)
        r.save()
        cmdb_log.log_change(request,i,data['Model_Name'],data)
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(r)

@csrf_exempt
def model_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_model'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id'].split(',')
    for del_id in ids:
        i = Model.objects.filter(id=del_id)
        cmdb_log.log_deletion(request,i[0],i[0].Model_Name,data)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"}) 
    return HttpResponse(del_id)
