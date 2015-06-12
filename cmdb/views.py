#_*_ coding: utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.admin.models import LogEntry
from cmdb.models import *
import json
import datetime

from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
import cmdb_log
@csrf_exempt
def login(request):
    json_str =request.body
    data = json.loads(json_str)
    username = data['username']
    pwd = data['pwd']
    user = auth.authenticate(username=username, password=pwd)
    if user is not None and user.is_active:
        request.session.set_expiry(3600)
        auth.login(request, user)
        result = 'ok'
        cmdb_log.log_login(username,result)
    else:
        result = 'fail'
        cmdb_log.log_login(username,result)
    r = {"result":result}
    r_json = json.dumps(r)
    return HttpResponse(r_json)

def logout(request):
    if request.user.is_authenticated():
        username = request.user.username
        auth.logout(request)
        cmdb_log.log_logoff(username)
        return HttpResponseRedirect("http://cmdb.ops.creditease.corp/ops/cmdb/html/login.html")
    else:
        return HttpResponseRedirect("http://cmdb.ops.creditease.corp/ops/cmdb/html/login.html")

def islogin(request):
    if not request.user.is_authenticated():
        result = 'fail'
        r = {"result":result}
        r_json = json.dumps(r)
        return HttpResponse(r_json)
    else:
        result = 'login'
        r = {"result":result}
        r_json = json.dumps(r)
        return HttpResponse(r_json)
def get_userinfo(request):
    return HttpResponse(request.user)
    
def get_user_list(request):
    #return render(request,'user.html')
    return HttpResponseRedirect("http://cmdb.ops.creditease.corp/cmdb/admin/auth/user/")
@csrf_exempt
def get_login_log(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    pageIndex = request.POST.get('pageIndex',0)
    pageSize = request.POST.get('pageSize',100)
    sortField = request.POST.get('sortField','action_time')
    sortOrder = request.POST.get('sortOrder','desc')
    start = int(pageIndex)*int(pageSize)
    stop = int(pageIndex)*int(pageSize) + int(pageSize)
    log_list = []
    if key == 'all':
        if sortOrder == 'asc':
            logs = Loginlog.objects.all().order_by(sortField)
        else:
            logs = Loginlog.objects.all().order_by('-'+sortField)
        for log in logs:
            action_time = log.action_time+datetime.timedelta(hours=8)
            log_d = {
                 'user':log.user,
                 'message':log.message,
                 'action_time':action_time.strftime('%Y-%m-%d  %H:%M:%S')
                }
            log_list.append(log_d)
        data = {"total":len(log_list),"data":log_list[start:stop]}
        json_r = json.dumps(data)
    if key == 'user':
        user = request.POST['search']
        if user == '':
            user = 'admin'
        if sortOrder == 'asc':
            logs = Loginlog.objects.filter(user=user).order_by(sortField)
        else:
            logs = Loginlog.objects.filter(user=user).order_by('-'+sortField)      
        for log in logs:
            action_time = log.action_time+datetime.timedelta(hours=8)
            log_d = {
                 'user':log.user,
                 'message':log.message,
                 'action_time':action_time.strftime('%Y-%m-%d  %H:%M:%S')
                }
            log_list.append(log_d)
        data = {"total":len(log_list),"data":log_list[start:stop]}
        json_r = json.dumps(data)
    return HttpResponse(json_r)
@csrf_exempt
def get_op_log(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    pageIndex = request.POST.get('pageIndex',0)
    pageSize = request.POST.get('pageSize',100)
    sortField = request.POST.get('sortField','action_time')
    sortOrder = request.POST.get('sortOrder','desc')
    start = int(pageIndex)*int(pageSize)
    stop = int(pageIndex)*int(pageSize) + int(pageSize)
    log_list = []
    if key == 'all':
        if sortOrder == 'asc':
            logs =LogEntry.objects.all().order_by(sortField)
        else:
            logs = LogEntry.objects.all().order_by('-'+sortField)
        for log in logs:
            user = User.objects.get(id=log.user_id).username
            action_time = log.action_time+datetime.timedelta(hours=8)
            log_d = {
                 'user':user,
                 'content_type':ContentType.objects.get(id = log.content_type_id).name,
                 'action_flag':log.action_flag.__str__(),
                 'object_repr':log.object_repr,
                 'change_message':log.change_message,
                 'action_time':action_time.strftime('%Y-%m-%d  %H:%M:%S')
                }
            log_list.append(log_d)
        data = {"total":len(log_list),"data":log_list[start:stop]}
        json_r = json.dumps(data) 
    if key == 'user':
        user = request.POST['search']
        if user == '':
            user = 'admin'
        if sortOrder == 'asc':
            logs = LogEntry.objects.filter(user=user).order_by(sortField)
        else:
            logs = LogEntry.objects.filter(user=user).order_by('-'+sortField)
        for log in logs:
            user = User.objects.get(id=log.user_id).username
            action_time = LogEntry.action_time+datetime.timedelta(hours=8)
            log_d = {
                 'user':user,
                 'content_type':ContentType.objects.get(id = log.content_type_id).name,
                 'action_flag':log.action_flag.__str__(),
                 'object_repr':log.object_repr,
                 'change_message':log.change_message,
                 'action_time':action_time.strftime('%Y-%m-%d  %H:%M:%S')
                }
            log_list.append(log_d)
        data = {"total":len(log_list),"data":log_list[start:stop]}
        json_r = json.dumps(data)
    return HttpResponse(json_r)
