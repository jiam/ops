# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import Department 
import json
import urllib
import cmdb_log

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def department_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        department_r = list(Department.objects.all().values())
        data = {"total":len(department_r),"data":department_r[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        department_r = list(Department.objects.filter(id=id).values())[0]
        json_r = json.dumps(department_r)
    else:
        department_r = list(Department.objects.filter(Department_Name__contains=key).values())
        json_r = json.dumps(department_r)
    return HttpResponse(json_r)

@csrf_exempt
def department_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        department_r = list(Department.objects.filter(id=data['id']).values())[0]
        json_r = json.dumps(department_r)
    if key == 'Department_Name':
        department_r = list(Department.objects.filter(Department_Name__contains=data['Department_Name']).values())[0]
        json_r = json.dumps(department_r)
    return HttpResponse(json_r)

@csrf_exempt  
def department_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_department'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        i = Department.objects.filter(id=data['id'])
        message = cmdb_log.cmp(list(i.values())[0],data)
        i.update(Department_Name = data['Department_Name'],Department_Contact = data['Department_Contact'])
        cmdb_log.log_change(request,i[0],data['Department_Name'],message)
    else:
        i = Department(Department_Name = data['Department_Name'],Department_Contact = data['Department_Contact'])
        i.save()
        cmdb_log.log_addition(request,i,data['Department_Name'],data)
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(json_r)

@csrf_exempt
def department_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_department'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id']
    for del_id in ids:
        i = Department.objects.filter(id=del_id)
        cmdb_log.log_deletion(request,i[0],i[0].Department_Name,data)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)
