# -*- coding: utf-8 -*-
from __future__ import division
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Count
from cmdb.models import *
import json

from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
    
def dashboard_host(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/ops/cmdb/html/login.html")
    physicals = HostPhysical.objects.all()
    virtuals = HostVirtual.objects.all()
    data = {'x':["物理主机","虚拟主机"],'y':[len(physicals),len(virtuals)]}
    j_data = json.dumps(data)
    return HttpResponse(j_data)

def dashboard_os(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/ops/cmdb/html/login.html")
    data = []
    oss = list(HostVirtual.objects.values('os').annotate(dcount=Count('os')))
    count = len(HostVirtual.objects.all())
    for os in  oss:
        os_id = os['os']
        os_name =  OS.objects.get(id=os_id).OS_Name
        #percent = os['dcount'] / count
        percent = os['dcount']
        data.append([os_name, percent])
    j_data = json.dumps(data)
    return HttpResponse(j_data)
        
        
        
    
     
