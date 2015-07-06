from rest_framework.authtoken.models import Token
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from cmdb.models import *
import json

@csrf_exempt
def  get_token(request):
    json_str = request.body
    data = json.loads(json_str)
    username = data['username']
    password = data['password']  
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        token,created = Token.objects.get_or_create(user=user)
        result = {'result':token.key} 
        response = json.dumps(result)
        return HttpResponse(response)
    else:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)
@csrf_exempt
def get_idc(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        idcs = IDC.objects.all().values()
        return HttpResponse(json.dumps(idcs))
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    
        

