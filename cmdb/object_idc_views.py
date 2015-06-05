# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import IDC 
import json
import urllib
import cmdb_log
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def idc_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        idc_r = list(IDC.objects.all().values())
        data = {"total":len(idc_r),"data":idc_r[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        idc_r = list(IDC.objects.filter(id=id).values())[0]
        json_r = json.dumps(idc_r)
    else:
        idc_r = list(IDC.objects.filter(IDC_Name__contains=key).values())
        json_r = json.dumps(idc_r)
    return HttpResponse(json_r)

@csrf_exempt
def idc_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("http://10.100.30.174/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        idc_r = list(IDC.objects.filter(id=data['id']).values())[0]
        json_r = json.dumps(idc_r)
    if key == 'IDC_Name':
        idc_r = list(IDC.objects.filter(IDC_Name__contains=data['IDC_Name']).values())[0]
        json_r = json.dumps(idc_r)
    return HttpResponse(json_r)

@csrf_exempt  
def idc_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_idc'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)

    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        i = IDC.objects.filter(id=data['id'])
        message = cmdb_log.cmp(list(i.values())[0],data)
        i.update(IDC_Name = data['IDC_Name'],IDC_Location = data['IDC_Location'],IDC_Contact = data['IDC_Contact'],IDC_Phone = data['IDC_Phone'],IDC_Email = data['IDC_Email'])
        cmdb_log.log_change(request,i[0],data['IDC_Name'],message)
    else:
        i = IDC(IDC_Name = data['IDC_Name'],IDC_Location = data['IDC_Location'],IDC_Contact = data['IDC_Contact'],IDC_Phone = data['IDC_Phone'],IDC_Email = data['IDC_Email'])
        i.save()
        cmdb_log.log_addition(request,i,data['IDC_Name'],data)
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(json_r)

@csrf_exempt
def idc_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_idc'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id'].split(',')
    for del_id in ids:
        i = IDC.objects.filter(id=del_id)
        cmdb_log.log_deletion(request,i[0],i[0].IDC_Name,data)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)
