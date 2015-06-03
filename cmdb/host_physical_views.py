# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import *
import json
import urllib

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect

@csrf_exempt  
def physical_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    physical_list = []
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        sortField = request.POST.get('sortField','SN')
        sortOrder = request.POST.get('sortOrder','asc')
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        if sortOrder == 'asc':
            physicals = HostPhysical.objects.select_related().all().order_by(sortField)
        else:
            physicals = HostPhysical.objects.select_related().all().order_by('-'+sortField)
        for physical in physicals:
            physical_d = {'id':physical.id,
                          'HostName':physical.HostName,
                          'Status':physical.Status,
                          'Asset_SN':physical.Asset_SN,
                          'SN':physical.SN,
                          'Vendor_id':physical.vendor.Vendor_Name,
                          'Service_id':physical.service.Service_Name,
                          'Model_id':physical.model.Model_Name,
                          'Manage_IP':physical.Manage_IP,
                          'RAC_IP':physical.RAC_IP,
                          'IDC_id':physical.idc.IDC_Name,
                          'Rack_id':physical.rack.Rack_Name,
                          }            
            physical_list.append(physical_d)
        data = {"total":len(physical_list),"data":physical_list[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        physical = HostPhysical.objects.get(id=id)
        physical_d = {'id':physical.id,
                      'HostName':physical.HostName,
                      'Status':physical.Status,
                      'Asset_SN':physical.Asset_SN,
                      'SN':physical.SN,
                      'Vendor_id':physical.vendor.id,
                      'Model_id':physical.model.id,
                      'OS_id':physical.os.id,
                      'Kernel_id':physical.kernel.id,
                      'Service_id':physical.service.id,
                      'Department_id':physical.department.id,
                      'IDC_id':physical.idc.id,
                      'Zone_id':physical.zone.id,
                      'Rack_id':physical.rack.id,
                      'Rack_Position':physical.Rack_Position,
                      'Manage_IP':physical.Manage_IP,
                      'RAC_IP':physical.RAC_IP,
                      'CPU_id':physical.cpu.id,
                      'CPU_Number':physical.CPU_Number,
                      'Memory_id':physical.memory.id,
                      'Memory_Number':physical.Memory_Number,
                      'Memory_Size':physical.Memory_Size,
                      'Disk_id':physical.disk.id,
                      'Disk_Number':physical.Disk_Number,
                      'Disk_Size':physical.Disk_Size,
                      'RAID_id':physical.raid.id,
                      'RAID_Battery':physical.RAID_Battery,
                      'RAID_Level':physical.RAID_Level,
                      'Purchasing_Time':str(physical.Purchasing_Time),
                      'Guarantee_Time':str(physical.Guarantee_Time),
                      'Change_Time':str(physical.Change_Time),
                      'Up_Time':str(physical.Up_Time),
                      'Change_Info':physical.Change_Info,
                      'Remarks':physical.Remarks
                      }            
        json_r = json.dumps(physical_d)
    elif key == 'hostname':
        hostname = request.POST.get('search')
        physicals= HostPhysical.objects.filter(HostName__contains=hostname)
        for physical in physicals:
            physical_d = {'id':physical.id,
                          'HostName':physical.HostName,
                          'Status':physical.Status,
                          'Asset_SN':physical.Asset_SN,
                          'SN':physical.SN,
                          'Vendor_id':physical.vendor.Vendor_Name,
                          'Service_id':physical.service.Service_Name,
                          'Model_id':physical.model.Model_Name,
                          'Manage_IP':physical.Manage_IP,
                          'RAC_IP':physical.RAC_IP,
                          'IDC_id':physical.idc.IDC_Name,
                          'Rack_id':physical.rack.Rack_Name,
                          }            
            physical_list.append(physical_d)
        data = {"total":len(physical_list),"data":physical_list}
        json_r = json.dumps(data)
    elif key == 'sn':
        sn = request.POST.get('search')
        physicals= HostPhysical.objects.filter(SN__contains=sn)
        for physical in physicals:
            physical_d = {'id':physical.id,
                          'HostName':physical.HostName,
                          'Status':physical.Status,
                          'Asset_SN':physical.Asset_SN,
                          'SN':physical.SN,
                          'Vendor_id':physical.vendor.Vendor_Name,
                          'Service_id':physical.service.Service_Name,
                          'Model_id':physical.model.Model_Name,
                          'Manage_IP':physical.Manage_IP,
                          'RAC_IP':physical.RAC_IP,
                          'IDC_id':physical.idc.IDC_Name,
                          'Rack_id':physical.rack.Rack_Name,
                          }            
            physical_list.append(physical_d)
        data = {"total":len(physical_list),"data":physical_list}
        json_r = json.dumps(data)
    elif key == 'asset_sn':
        asset_sn = request.POST.get('search')
        physicals= HostPhysical.objects.filter(Asset_SN__contains=asset_sn)
        for physical in physicals:
            physical_d = {'id':physical.id,
                          'HostName':physical.HostName,
                          'Status':physical.Status,
                          'Asset_SN':physical.Asset_SN,
                          'SN':physical.SN,
                          'Vendor_id':physical.vendor.Vendor_Name,
                          'Service_id':physical.service.Service_Name,
                          'Model_id':physical.model.Model_Name,
                          'Manage_IP':physical.Manage_IP,
                          'RAC_IP':physical.RAC_IP,
                          'IDC_id':physical.idc.IDC_Name,
                          'Rack_id':physical.rack.Rack_Name,
                          }            
            physical_list.append(physical_d)
        data = {"total":len(physical_list),"data":physical_list}
        json_r = json.dumps(data)
    elif key == 'ip':
        ip = request.POST.get('search')
        physicals= HostPhysical.objects.filter(Manage_IP__contains=ip)
        for physical in physicals:
            physical_d = {'id':physical.id,
                          'HostName':physical.HostName,
                          'Status':physical.Status,
                          'Asset_SN':physical.Asset_SN,
                          'SN':physical.SN,
                          'Vendor_id':physical.vendor.Vendor_Name,
                          'Service_id':physical.service.Service_Name,
                          'Model_id':physical.model.Model_Name,
                          'Manage_IP':physical.Manage_IP,
                          'RAC_IP':physical.RAC_IP,
                          'IDC_id':physical.idc.IDC_Name,
                          'Rack_id':physical.rack.Rack_Name,
                          }            
            physical_list.append(physical_d)
        data = {"total":len(physical_list),"data":physical_list}
        json_r = json.dumps(data)
    return HttpResponse(json_r)


@csrf_exempt
def physical_get_details(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    id = request.POST.get('id')
    physical = HostPhysical.objects.get(id=id)
    physical_d = {'id':physical.id,
                  'HostName':physical.HostName,
                  'Status':physical.Status,
                  'Asset_SN':physical.Asset_SN,
                  'SN':physical.SN,
                  'Vendor_id':physical.vendor.Vendor_Name,
                  'Model_id':physical.model.Model_Name,
                  'OS_id':physical.os.OS_Name,
                  'Kernel_id':physical.kernel.Kernel_Name,
                  'Service_id':physical.service.Service_Name,
                  'Department_id':physical.department.Department_Name,
                  'IDC_id':physical.idc.IDC_Name,
                  'Zone_id':physical.zone.Zone_Name,
                  'Rack_id':physical.rack.Rack_Name,
                  'Rack_Position':physical.Rack_Position,
                  'Manage_IP':physical.Manage_IP,
                  'RAC_IP':physical.RAC_IP,
                  'CPU_id':physical.cpu.CPU_Type,
                  'CPU_Number':physical.CPU_Number,
                  'Memory_id':physical.memory.Memory_Type,
                  'Memory_Number':physical.Memory_Number,
                  'Memory_Size':physical.Memory_Size,
                  'Disk_id':physical.disk.Disk_Type,
                  'Disk_Number':physical.Disk_Number,
                  'Disk_Size':physical.Disk_Size,
                  'RAID_id':physical.raid.RAID_Type,
                  'RAID_Battery':physical.RAID_Battery,
                  'RAID_Level':physical.RAID_Level,
                  'Purchasing_Time':str(physical.Purchasing_Time),
                  'Guarantee_Time':str(physical.Guarantee_Time),
                  'Change_Time':str(physical.Change_Time),
                  'Up_Time':str(physical.Up_Time),
                  'Change_Info':physical.Change_Info,
                  'Remarks':physical.Remarks
                  }            
    json_r = json.dumps(physical_d)
    return HttpResponse(json_r)

@csrf_exempt
def physical_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("http://10.100.30.174/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    physical_list = []
    key = data['key']
    search = data['search']
    if key == 'hostname':
        physicals= HostPhysical.objects.filter(HostName__contains=search)
        for physical in physicals:
            physical_d = {'id':physical.id,
                          'HostName':physical.HostName,
                          'Status':physical.Status,
                          'Asset_SN':physical.Asset_SN,
                          'SN':physical.SN,
                          'Vendor_id':physical.vendor.Vendor_Name,
                          'Service_id':physical.service.Service_Name,
                          'Model_id':physical.model.Model_Name,
                          'Manage_IP':physical.Manage_IP,
                          'RAC_IP':physical.RAC_IP,
                          'IDC_id':physical.idc.IDC_Name,
                          'Rack_id':physical.rack.Rack_Name,
                          }            
            physical_list.append(physical_d)
        data = {"total":len(physical_list),"data":physical_list}
        json_r = json.dumps(data)
    if key == 'ip':
        physicals= HostPhysical.objects.filter(Manage_IP=key)
        for physical in physicals:
            physical_d = {'id':physical.id,
                          'HostName':physical.HostName,
                          'Status':physical.Status,
                          'Asset_SN':physical.Asset_SN,
                          'SN':physical.SN,
                          'Vendor_id':physical.vendor.Vendor_Name,
                          'Service_id':physical.service.Service_Name,
                          'Model_id':physical.model.Model_Name,
                          'Manage_IP':physical.Manage_IP,
                          'RAC_IP':physical.RAC_IP,
                          'IDC_id':physical.idc.IDC_Name,
                          'Rack_id':physical.rack.Rack_Name,
                          }            
            physical_list.append(physical_d)
        data = {"total":len(physical_list),"data":physical_list}
        json_r = json.dumps(data)
    return HttpResponse(json_r)

@csrf_exempt  
def physical_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_hostphysical'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        h = HostPhysical.objects.filter(id=data['id'])
        vendor = Vendor.objects.get(id=data['Vendor_id'])
        model = Model.objects.get(id=data['Model_id'])
        os = OS.objects.get(id=data['OS_id'])
        kernel = Kernel.objects.get(id=data['Kernel_id'])
        service = Service.objects.get(id=data['Service_id'])
        department = Department.objects.get(id=data['Department_id'])
        idc = IDC.objects.get(id=data['IDC_id'])
        rack = Rack.objects.get(id=data['Rack_id'])
        cpu = CPU.objects.get(id=data['CPU_id'])
        memory = Memory.objects.get(id=data['Memory_id'])
        disk = Disk.objects.get(id=data['Disk_id'])
        raid = RAID.objects.get(id=data['RAID_id'])
        zone = Zone.objects.get(id=data['Zone_id'])
        h.update(SN = data['SN'],
             Asset_SN = data['Asset_SN'],
             vendor = vendor,
             model = model,
             HostName = data['HostName'],
             os = os,
             kernel = kernel,
             service = service,
             department = department,
             idc = idc,
             rack = rack,
             Rack_Position = data['Rack_Position'],
             cpu = cpu,
             CPU_Number = data['CPU_Number'],           
             memory = memory,
             Memory_Number = data['Memory_Number'],
             Memory_Size = data['Memory_Size'],
             disk = disk,
             Disk_Number = data['Disk_Number'],
             Disk_Size = data['Disk_Size'],
             raid = raid,
             RAID_Battery = data['RAID_Battery'],
             RAID_Level = data['RAID_Level'],
             Status = data['Status_id'],
             zone = zone,
             Manage_IP = data['Manage_IP'],
             RAC_IP = data['RAC_IP'],
             Purchasing_Time = data['Purchasing_Time'][0:10],
             Guarantee_Time = data['Guarantee_Time'][0:10],
             Change_Time = data['Change_Time'][0:10],
             Up_Time = data['Up_Time'][0:10],
             Change_Info = data['Change_Info'],
             Remarks = data['Remarks']
                 )
        json_r = json.dumps({"result":"save sucess"})
        return HttpResponse(json_r)
    else:
        vendor = Vendor.objects.get(id=data['Vendor_id'])
        model = Model.objects.get(id=data['Model_id'])
        os = OS.objects.get(id=data['OS_id'])
        kernel = Kernel.objects.get(id=data['Kernel_id'])
        service = Service.objects.get(id=data['Service_id'])
        department = Department.objects.get(id=data['Department_id'])
        idc = IDC.objects.get(id=data['IDC_id'])
        rack = Rack.objects.get(id=data['Rack_id'])
        cpu = CPU.objects.get(id=data['CPU_id'])
        memory = Memory.objects.get(id=data['Memory_id'])
        disk = Disk.objects.get(id=data['Disk_id'])
        raid = RAID.objects.get(id=data['RAID_id'])
        zone = Zone.objects.get(id=data['Zone_id'])
        h = HostPhysical(SN = data['SN'],
             Asset_SN = data['Asset_SN'],
             vendor = vendor,
             model = model,
             HostName = data['HostName'],
             os = os,
             kernel = kernel,
             service = service,
             department = department,
             idc = idc,
             rack = rack,
             Rack_Position = data['Rack_Position'],
             cpu = cpu,
             CPU_Number = data['CPU_Number'],
             memory = memory,
             Memory_Number = data['Memory_Number'],
             Memory_Size = data['Memory_Size'],
             disk = disk,
             Disk_Number = data['Disk_Number'],
             Disk_Size = data['Disk_Size'],
             raid = raid,
             RAID_Battery = data['RAID_Battery'],
             RAID_Level = data['RAID_Level'],
             Status = data['Status_id'],
             zone = zone,
             Manage_IP = data['Manage_IP'],
             RAC_IP = data['RAC_IP'],
             Purchasing_Time = data['Purchasing_Time'][0:10],
             Guarantee_Time = data['Guarantee_Time'][0:10],
             Change_Time = data['Change_Time'][0:10],
             Up_Time = data['Up_Time'][0:10],
             Change_Info = data['Change_Info'],
             Remarks = data['Remarks']
                 )
	h.save()
        json_r = json.dumps({"result":"save sucess"})
        return HttpResponse(json_r)

@csrf_exempt
def physical_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_hostphysical'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id']
    for del_id in ids:
        i = HostPhysical.objects.filter(id=del_id)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)
