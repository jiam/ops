# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import *
import json
import urllib
import cmdb_log
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
#@cache_page(60 * 15)
def physical_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    pageIndex = request.POST.get('pageIndex',0)
    pageSize = request.POST.get('pageSize',100)
    sortField = request.POST.get('sortField','SN')
    sortOrder = request.POST.get('sortOrder','asc')
    start = int(pageIndex)*int(pageSize)
    stop = int(pageIndex)*int(pageSize) + int(pageSize)
    physical_list = []
    #分页返回全部
    if key == 'all':
        if sortOrder == 'asc':
            physicals = HostPhysical.objects.order_by(sortField)[start:stop]
        else:
            physicals = HostPhysical.objects.order_by('-'+sortField)[start:stop]
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
        data = {"total":HostPhysical.objects.count(),"data":physical_list}
        json_r = json.dumps(data)
    elif key == 'id':  #返回编辑信息
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
                      'User':physical.User,
                      'UseInfo':physical.UseInfo,
                      'IDC_id':physical.idc.id,
                      'Zone_id':physical.zone.id,
                      'Rack_id':physical.rack.id,
                      'Rack_Position':physical.Rack_Position,
                      'Manage_IP':physical.Manage_IP,
                      'RAC_IP':physical.RAC_IP,
                      'NAS_IP':physical.NAS_IP,
                      'VIP':physical.VIP,
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
                      'HBA_id':physical.hba.id,
                      'HBA_Number':physical.HBA_Number,
                      'PCIE_id':physical.pcie.id,
                      'PCIE_Number':physical.PCIE_Number,
                      'NIC_id':physical.nic.id,
                      'NIC_Number':physical.NIC_Number,
                      'Purchasing_Time':str(physical.Purchasing_Time),
                      'Guarantee_Time':str(physical.Guarantee_Time),
                      'Change_Time':str(physical.Change_Time),
                      'Up_Time':str(physical.Up_Time),
                      'Change_Info':physical.Change_Info,
                      'Remarks':physical.Remarks
                      }            
        json_r = json.dumps(physical_d)
    else:      #按条件查找
        search = request.POST.get('search')
        params = { key+'__startswith':search}
        queryset= HostPhysical.objects.filter(**params)
        physicals= queryset[start:stop]
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
        data = {"total":queryset.count(),"data":physical_list}
        json_r = json.dumps(data)
    return HttpResponse(json_r)


@csrf_exempt
def physical_get_details(request,id):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    #id = request.POST.get('id')
    id = id
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
                  'User':physical.User,
                  'UseInfo':physical.UseInfo,
                  'IDC_id':physical.idc.IDC_Name,
                  'Zone_id':physical.zone.Zone_Name,
                  'Rack_id':physical.rack.Rack_Name,
                  'Rack_Position':physical.Rack_Position,
                  'Manage_IP':physical.Manage_IP,
                  'RAC_IP':physical.RAC_IP,
                  'NAS_IP':physical.NAS_IP,
                  'VIP':physical.VIP,
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
                  'HBA_id':physical.hba.HBA_Type,
                  'HBA_Number':physical.HBA_Number,
                  'PCIE_id':physical.pcie.PCIE_Type,
                  'PCIE_Number':physical.PCIE_Number,
                  'NIC_id':physical.nic.NIC_Type,
                  'NIC_Number':physical.NIC_Number,
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
        vendor = Vendor.objects.get(id=data['vendor_id'])
        model = Model.objects.get(id=data['model_id'])
        os = OS.objects.get(id=data['os_id'])
        kernel = Kernel.objects.get(id=data['kernel_id'])
        service = Service.objects.get(id=data['service_id'])
        department = Department.objects.get(id=data['department_id'])
        idc = IDC.objects.get(id=data['idc_id'])
        rack = Rack.objects.get(id=data['rack_id'])
        cpu = CPU.objects.get(id=data['cpu_id'])
        memory = Memory.objects.get(id=data['memory_id'])
        disk = Disk.objects.get(id=data['disk_id'])
        hba = HBA.objects.get(id=data['hba_id'])
        pcie = PCIE.objects.get(id=data['pcie_id'])
        nic = NIC.objects.get(id=data['nic_id'])
        raid = RAID.objects.get(id=data['raid_id'])
        zone = Zone.objects.get(id=data['zone_id'])
        message = cmdb_log.cmp(data,list(h.values())[0])
        h.update(SN = data['SN'],
             Asset_SN = data['Asset_SN'],
             vendor = vendor,
             model = model,
             HostName = data['HostName'],
             os = os,
             kernel = kernel,
             service = service,
             department = department,
             User = data['User'],
             UseInfo = data['UseInfo'],
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
             hba = hba,
             HBA_Number = data['HBA_Number'],
             pcie = pcie,
             PCIE_Number = data['PCIE_Number'],
             nic = nic,
             NIC_Number = data['NIC_Number'],
             Status = data['Status'],
             zone = zone,
             Manage_IP = data['Manage_IP'],
             RAC_IP = data['RAC_IP'],
             NAS_IP = data['NAS_IP'],
             VIP = data['VIP'],
             Purchasing_Time = data['Purchasing_Time'][0:10],
             Guarantee_Time = data['Guarantee_Time'][0:10],
             Change_Time = data['Change_Time'][0:10],
             Up_Time = data['Up_Time'][0:10],
             Change_Info = data['Change_Info'],
             Remarks = data['Remarks']
                 )
        cmdb_log.log_change(request,h[0],data['Manage_IP'],message)
        json_r = json.dumps({"result":"save sucess"})
        return HttpResponse(json_r)
    else:
        vendor = Vendor.objects.get(id=data['vendor_id'])
        model = Model.objects.get(id=data['model_id'])
        os = OS.objects.get(id=data['os_id'])
        kernel = Kernel.objects.get(id=data['kernel_id'])
        service = Service.objects.get(id=data['service_id'])
        department = Department.objects.get(id=data['department_id'])
        idc = IDC.objects.get(id=data['idc_id'])
        rack = Rack.objects.get(id=data['rack_id'])
        cpu = CPU.objects.get(id=data['cpu_id'])
        memory = Memory.objects.get(id=data['memory_id'])
        disk = Disk.objects.get(id=data['disk_id'])
        raid = RAID.objects.get(id=data['raid_id'])
        hba = HBA.objects.get(id=data['hba_id'])
        pcie = PCIE.objects.get(id=data['pcie_id'])
        nic = NIC.objects.get(id=data['nic_id'])
        zone = Zone.objects.get(id=data['zone_id'])
        h = HostPhysical(SN = data['SN'],
             Asset_SN = data['Asset_SN'],
             vendor = vendor,
             model = model,
             HostName = data['HostName'],
             os = os,
             kernel = kernel,
             service = service,
             department = department,
             User = data['User'],
             UseInfo = data['UseInfo'],
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
             hba = hba,
             HBA_Number = data['HBA_Number'],
             pcie = pcie,
             PCIE_Number = data['PCIE_Number'],
             nic = nic,
             NIC_Number = data['NIC_Number'],
             Status = data['Status'],
             zone = zone,
             Manage_IP = data['Manage_IP'],
             RAC_IP = data['RAC_IP'],
             NAS_IP = data['NAS_IP'],
             VIP = data['VIP'],
             Purchasing_Time = data['Purchasing_Time'][0:10],
             Guarantee_Time = data['Guarantee_Time'][0:10],
             Change_Time = data['Change_Time'][0:10],
             Up_Time = data['Up_Time'][0:10],
             Change_Info = data['Change_Info'],
             Remarks = data['Remarks']
                 )
	h.save()
        cmdb_log.log_addition(request,h,data['Manage_IP'],data)
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
    ids = data['id'].split(',')
    for del_id in ids:
        i = HostPhysical.objects.filter(id=del_id)
        cmdb_log.log_deletion(request,i[0],i[0].Manage_IP,data)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)

@csrf_exempt
def physical_copy(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_hostphysical'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    copy_id = data['id']
    source = HostPhysical.objects.filter(id=copy_id)
    mid = source.values()[0]
    mid.pop('id')
    mid['HostName']= mid['HostName']+'copy'
    dest = HostPhysical(**mid) 
    cmdb_log.log_addition(request,dest,dest.Manage_IP,data)
    dest.save()
    json_r = json.dumps({"result":"copy sucess"})
    return HttpResponse(json_r)
