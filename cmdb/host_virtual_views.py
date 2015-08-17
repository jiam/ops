# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import *
import json

from django.views.decorators.csrf import csrf_exempt
import cmdb_log

@csrf_exempt  
def virtual_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    pageIndex = request.POST.get('pageIndex',0)
    pageSize = request.POST.get('pageSize',100)
    sortField = request.POST.get('sortField','Manage_IP')
    sortOrder = request.POST.get('sortOrder','asc')
    start = int(pageIndex)*int(pageSize)
    stop = int(pageIndex)*int(pageSize) + int(pageSize)
    virtual_list = []
    if key == 'all':
        if sortOrder == 'asc':
            virtuals = HostVirtual.objects.order_by(sortField)[start:stop]
        else:
            virtuals = HostVirtual.objects.order_by('-'+sortField)[start:stop]
        for virtual in virtuals:
            virtual_d = {'id':virtual.id,
                          'HostName':virtual.HostName,
                          'Status':virtual.Status,
                          'Use_Info':virtual.Use_Info,
                          'User':virtual.User,
                          'Department_id':virtual.department.Department_Name,
                          'Manage_IP':virtual.Manage_IP,
                          'Physical_Host_IP': virtual.Physical_Host_IP,
                          'SSH_Port':virtual.SSH_Port,
                          }            
            virtual_list.append(virtual_d)
        data = {"total":HostVirtual.objects.count(),"data":virtual_list}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        virtual = HostVirtual.objects.get(id=id)
        virtual_d = {'id':virtual.id,
                     'HostName': virtual.HostName,
                     'OS_id': virtual.os.id,
                     'Kernel_id': virtual.kernel.id,
                     'Deploy_Path': virtual.Deploy_Path,
                     'Service_id': virtual.service.id,
                     'Department_id': virtual.department.id,
                     'User': virtual.User,
                     'vCPU_Number': virtual.vCPU_Number,           
                     'Memory_Size': virtual.Memory_Size,
                     'Disk_Size': virtual.Disk_Size,
                     'Status': virtual.Status,
                     'Manage_IP': virtual.Manage_IP,
                     'VIP': virtual.VIP,
                     'NAS_IP': virtual.NAS_IP,
                     'Physical_Host_IP': virtual.Physical_Host_IP,
                     'SSH_Port': virtual.SSH_Port,
                     'Application_Time': str(virtual.Application_Time),
                     'Change_Time': str(virtual.Change_Time),
                     'Use_Period': virtual.Use_Period,
                     'Use_Info': virtual.Use_Info,
                     'Up_Time': str(virtual.Up_Time),
                     'Change_Info': virtual.Change_Info,
                     'Remarks': virtual.Remarks
                      }            
        json_r = json.dumps(virtual_d)
    else: 
        
        search = request.POST.get('search')
        params = { key+'__startswith':search}
        queryset= HostVirtual.objects.filter(**params)
        virtuals= queryset[start:stop]
        for virtual in virtuals:
            virtual_d = {'id':virtual.id,
                          'HostName':virtual.HostName,
                          'Status':virtual.Status,
                          'Use_Info':virtual.Use_Info,
                          'User':virtual.User,
                          'Department_id':virtual.department.Department_Name,
                          'Manage_IP':virtual.Manage_IP,
                          'Physical_Host_IP': virtual.Physical_Host_IP,
                          'SSH_Port':virtual.SSH_Port,
                          }            
            virtual_list.append(virtual_d)
        data = {"total":queryset.count(),"data":virtual_list}
        json_r = json.dumps(data)
    return HttpResponse(json_r)


@csrf_exempt
def virtual_get_details(request,id):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    #id = request.POST.get('id')
    id = id
    virtual = HostVirtual.objects.get(id=id)
    virtual_d = {'id':virtual.id,
                 'HostName': virtual.HostName,
                 'OS_id': virtual.os.OS_Name,
                 'Kernel_id': virtual.kernel.Kernel_Name,
                 'Deploy_Path': virtual.Deploy_Path,
                 'Service_id': virtual.service.Service_Name,
                 'Department_id': virtual.department.Department_Name,
                 'User': virtual.User,
                 'vCPU_Number': virtual.vCPU_Number,           
                 'Memory_Size': virtual.Memory_Size,
                 'Disk_Size': virtual.Disk_Size,
                 'Status': virtual.Status,
                 'Manage_IP': virtual.Manage_IP,
                 'VIP': virtual.VIP,
                 'NAS_IP': virtual.NAS_IP,
                 'Physical_Host_IP': virtual.Physical_Host_IP,
                 'SSH_Port': virtual.SSH_Port,
                 'Application_Time': str(virtual.Application_Time),
                 'Change_Time': str(virtual.Change_Time),
                 'Use_Period': virtual.Use_Period,
                 'Use_Info': virtual.Use_Info,
                 'Up_Time': str(virtual.Up_Time),
                 'Change_Info': virtual.Change_Info,
                 'Remarks': virtual.Remarks
                  }            

    json_r = json.dumps(virtual_d)
    return HttpResponse(json_r)

@csrf_exempt
def virtual_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    virtual_list = []
    key = data['key']
    search = data['search']
    if key == 'hostname':
        virtuals= HostVirtual.objects.filter(HostName__contains=search)
        for virtual in virtuals:
            virtual_d = {'id':virtual.id,
                          'HostName':virtual.HostName,
                          'Status':virtual.Status,
                          'Asset_SN':virtual.Asset_SN,
                          'SN':virtual.SN,
                          'Vendor_id':virtual.vendor.Vendor_Name,
                          'Service_id':virtual.service.Service_Name,
                          'Model_id':virtual.model.Model_Name,
                          'Manage_IP':virtual.Manage_IP,
                          'RAC_IP':virtual.RAC_IP,
                          'IDC_id':virtual.idc.IDC_Name,
                          'Rack_id':virtual.rack.Rack_Name,
                          }            
            virtual_list.append(virtual_d)
        data = {"total":len(virtual_list),"data":virtual_list}
        json_r = json.dumps(data)
    if key == 'ip':
        virtuals= HostVirtual.objects.filter(Manage_IP=key)
        for virtual in virtuals:
            virtual_d = {'id':virtual.id,
                          'HostName':virtual.HostName,
                          'Status':virtual.Status,
                          'Asset_SN':virtual.Asset_SN,
                          'SN':virtual.SN,
                          'Vendor_id':virtual.vendor.Vendor_Name,
                          'Service_id':virtual.service.Service_Name,
                          'Model_id':virtual.model.Model_Name,
                          'Manage_IP':virtual.Manage_IP,
                          'RAC_IP':virtual.RAC_IP,
                          'IDC_id':virtual.idc.IDC_Name,
                          'Rack_id':virtual.rack.Rack_Name,
                          }            
            virtual_list.append(virtual_d)
        data = {"total":len(virtual_list),"data":virtual_list}
        json_r = json.dumps(data)
    return HttpResponse(json_r)

@csrf_exempt  
def virtual_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_hostvirtual'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        h = HostVirtual.objects.filter(id=data['id'])
        os = OS.objects.get(id=data['os_id'])
        kernel = Kernel.objects.get(id=data['kernel_id'])
        service = Service.objects.get(id=data['service_id'])
        department = Department.objects.get(id=data['department_id'])
        message = cmdb_log.cmp(data,list(h.values())[0])
        h.update(
             HostName = data['HostName'],
             os = os,
             kernel = kernel,
             Deploy_Path = data['Deploy_Path'],
             service = service,
             department = department,
             User = data['User'],
             vCPU_Number = data['vCPU_Number'],           
             Memory_Size = data['Memory_Size'],
             Disk_Size = data['Disk_Size'],
             Status = data['Status'],
             Manage_IP = data['Manage_IP'],
             VIP = data['VIP'],
             NAS_IP = data['NAS_IP'],
             Physical_Host_IP = data['Physical_Host_IP'],
             SSH_Port = data['SSH_Port'],
             Application_Time = data['Application_Time'][0:10],
             Change_Time = data['Change_Time'][0:10],
             Use_Period = data['Use_Period'],
             Use_Info = data['Use_Info'],
             Up_Time = data['Up_Time'][0:10],
             Change_Info = data['Change_Info'],
             Remarks = data['Remarks']
                 )
        cmdb_log.log_change(request,h[0],data['Manage_IP'],message)
        json_r = json.dumps({"result":"save sucess"})
        return HttpResponse(json_r)
    else:
        os = OS.objects.get(id=data['os_id'])
        kernel = Kernel.objects.get(id=data['kernel_id'])
        service = Service.objects.get(id=data['service_id'])
        department = Department.objects.get(id=data['department_id'])
        h = HostVirtual(
             HostName = data['HostName'],
             os = os,
             kernel = kernel,
             Deploy_Path = data['Deploy_Path'],
             service = service,
             department = department,
             User = data['User'],
             vCPU_Number = data['vCPU_Number'],           
             Memory_Size = data['Memory_Size'],
             Disk_Size = data['Disk_Size'],
             Status = data['Status'],
             Manage_IP = data['Manage_IP'],
             VIP = data['VIP'],
             NAS_IP = data['NAS_IP'],
             Physical_Host_IP = data['Physical_Host_IP'],
             SSH_Port = data['SSH_Port'],
             Application_Time = data['Application_Time'][0:10],
             Change_Time = data['Change_Time'][0:10],
             Use_Period = data['Use_Period'],
             Use_Info = data['Use_Info'],
             Up_Time = data['Up_Time'][0:10],
             Change_Info = data['Change_Info'],
             Remarks = data['Remarks']
                 )
	h.save()
        cmdb_log.log_addition(request,h,data['Manage_IP'],data)
        json_r = json.dumps({"result":"save sucess"})
        return HttpResponse(json_r)

@csrf_exempt
def virtual_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_hostvirtual'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id'].split(',')
    for del_id in ids:
        i = HostVirtual.objects.filter(id=del_id)
        cmdb_log.log_deletion(request,i[0],i[0].Manage_IP,data)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)


@csrf_exempt
def virtual_copy(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_hostvirtual'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    copy_id = data['id']
    source = HostVirtual.objects.filter(id=copy_id)
    mid = source.values()[0]
    mid.pop('id')
    mid['HostName']= mid['HostName']+'copy'
    dest = HostVirtual(**mid)
    cmdb_log.log_addition(request,dest,dest.Manage_IP,data)
    dest.save()
    json_r = json.dumps({"result":"copy sucess"})
    return HttpResponse(json_r)
