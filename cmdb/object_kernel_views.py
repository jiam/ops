# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import Kernel
import json
import urllib

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def kernel_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        kernel_r = list(Kernel.objects.all().values())
        data = {"total":len(kernel_r),"data":kernel_r[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        kernel_r = list(Kernel.objects.filter(id=id).values())[0]
        json_r = json.dumps(kernel_r)
    else:
        kernel_r = list(Kernel.objects.filter(Kernel_Name__contains=key).values())
        json_r = json.dumps(kernel_r)
    return HttpResponse(json_r)

@csrf_exempt
def kernel_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("http://10.100.30.174/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        kernel_r = list(Kernel.objects.filter(id=data['id']).values())[0]
        json_r = json.dumps(kernel_r)
    if key == 'Kernel_Name':
        kernel_r = list(Kernel.objects.filter(Kernel_Name__contains=data['Kernel_Name']).values())[0]
        json_r = json.dumps(kernel_r)
    return HttpResponse(json_r)

@csrf_exempt  
def kernel_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_kernel'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        i = Kernel.objects.filter(id=data['id'])
        i.update(Kernel_Name = data['Kernel_Name'])
    else:
        i = Kernel(Kernel_Name = data['Kernel_Name'])
        i.save()
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(json_r)
@csrf_exempt
def kernel_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_kernel'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id']
    for del_id in ids:
        i = Kernel.objects.filter(id=del_id)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)
