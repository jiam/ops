# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import Memory 
import json
import urllib

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def memory_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        memory_r = list(Memory.objects.all().values())
        data = {"total":len(memory_r),"data":memory_r[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        memory_r = list(Memory.objects.filter(id=id).values())[0]
        json_r = json.dumps(memory_r)
    else:
        memory_r = list(Memory.objects.filter(Memory_Type__contains=key).values())
        json_r = json.dumps(memory_r)
    return HttpResponse(json_r)

@csrf_exempt
def memory_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("http://10.100.30.174/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        memory_r = list(Memory.objects.filter(id=data['id']).values())[0]
        json_r = json.dumps(memory_r)
    if key == 'Memory_Vendor':
        memory_r = list(Memory.objects.filter(Memory_Type__contains=data['Memory_Vendor']).values())[0]
        json_r = json.dumps(memory_r)
    return HttpResponse(json_r)

@csrf_exempt  
def memory_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_memory'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        i = Memory.objects.filter(id=data['id'])
        i.update(Memory_Type = data['Memory_Type'])
    else:
        i = Memory(Memory_Type = data['Memory_Type'])
        i.save()
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(json_r)
@csrf_exempt
def memory_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_memory'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id']
    for del_id in ids:
        i = Memory.objects.filter(id=del_id)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)