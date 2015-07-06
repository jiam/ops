# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import  *
import json
import urllib
import cmdb_log

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def memory_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    memory_list = []
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        sortField = request.POST.get('sortField','SN')
        sortOrder = request.POST.get('sortOrder','asc')
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        if sortOrder == 'asc':
            memorys = Accessories_Memory.objects.select_related().all().order_by(sortField)
        else:
            memorys = Accessories_Memory.objects.select_related().all().order_by('-'+sortField)
        for memory in memorys:
            memory_d = {'id':memory.id,
                        'SN':memory.SN,
                        'Memory_Type':memory.Memory_Type.Memory_Type,
                        'Status':memory.Status,
                        'Host_SN':memory.Host_SN
                          }
            memory_list.append(memory_d)
        data = {"total":len(memory_list),"data":memory_list[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        memory_r = list(Accessories_Memory.objects.filter(id=id).values())[0]
        json_r = json.dumps(memory_r)
    elif key == 'sn':
        id = request.POST.get('sn')
        sn = request.POST.get('search')
        memorys = Accessories_Memory.objects.filter(SN=sn)
        for memory in memorys:
            memory_d = {'id':memory.id,
                        'SN':memory.SN,
                        'Memory_Type':memory.Memory_Type.Memory_Type,
                        'Status':memory.Status,
                        'Host_SN':memory.Host_SN
                          }
            memory_list.append(memory_d)
        data = {"total":len(memory_list),"data":memory_list}
        json_r = json.dumps(data)
    elif key == 'ip':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        sortField = request.POST.get('sortField','SN')
        sortOrder = request.POST.get('sortOrder','asc')
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        ip = request.POST.get('search')
        memorys = Accessories_Memory.objects.filter(Host_SN=ip)
        for memory in memorys:
            memory_d = {'id':memory.id,
                        'SN':memory.SN,
                        'Memory_Type':memory.Memory_Type.Memory_Type,
                        'Status':memory.Status,
                        'Host_SN':memory.Host_SN
                          }
            memory_list.append(memory_d)
        data = {"total":len(memory_list),"data":memory_list[start:stop]}
        json_r = json.dumps(data)
    return HttpResponse(json_r)

@csrf_exempt
def memory_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        memory_r = list(Accessories_Memory.objects.filter(id=data['id']).values())[0]
        json_r = json.dumps(memory_r)
    if key == 'Disk_Type':
        memory_r = list(Accessories_Memory.objects.filter(Disk_Type__contains=data['Disk_Type']).values())[0]
        json_r = json.dumps(memory_r)
    return HttpResponse(json_r)

@csrf_exempt  
def memory_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_accessories_memory'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        i = Accessories_Memory.objects.filter(id=data['id'])
        message = cmdb_log.cmp(list(i.values())[0],data)
        memory = Memory.objects.get(id=data['Memory_Type_id'])
        i.update(Host_SN = data['Host_SN'],
                 Status = data['Status'],
                 Memory_Type = memory,
                 SN = data['SN'],
                 )
        cmdb_log.log_change(request,i[0],data['Host_SN'],message)
    else:
        memory = Memory.objects.get(id=data['Memory_Type_id'])
        i = Accessories_Memory(Host_SN = data['Host_SN'],
                               Status = data['Status'],
                               Memory_Type = memory,
                               SN = data['SN'],
                               )
        i.save()
        cmdb_log.log_addition(request,i,data['SN'],data)
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(json_r)

@csrf_exempt
def memory_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_accessories_memory'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id'].split(',')
    for del_id in ids:
        i = Accessories_Memory.objects.filter(id=del_id)
        cmdb_log.log_deletion(request,i[0],i[0].SN,data)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)
