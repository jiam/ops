# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import CPU 
import json
import urllib

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def cpu_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        cpu_r = list(CPU.objects.all().values())
        data = {"total":len(cpu_r),"data":cpu_r[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        cpu_r = list(CPU.objects.filter(id=id).values())[0]
        json_r = json.dumps(cpu_r)
    else:
        cpu_r = list(CPU.objects.filter(CPU_Type__contains=key).values())
        json_r = json.dumps(cpu_r)
    return HttpResponse(json_r)

@csrf_exempt
def cpu_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("http://10.100.30.174/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        cpu_r = list(CPU.objects.filter(id=data['id']).values())[0]
        json_r = json.dumps(cpu_r)
    if key == 'CPU_Type':
        cpu_r = list(CPU.objects.filter(CPU_Type__contains=data['CPU_Type']).values())[0]
        json_r = json.dumps(cpu_r)
    return HttpResponse(json_r)

@csrf_exempt  
def cpu_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_rack'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        i = CPU.objects.filter(id=data['id'])
        i.update(CPU_Type = data['CPU_Type'],CPU_Cores = data['CPU_Cores'])
    else:
        i = CPU(CPU_Type = data['CPU_Type'],CPU_Cores = data['CPU_Cores'])
        i.save()
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(json_r)
@csrf_exempt
def cpu_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_rack'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id']
    for del_id in ids:
        i = CPU.objects.filter(id=del_id)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)
