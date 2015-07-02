from rest_framework.authtoken.models import Token
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
import json

@csrf_exempt
def  get_token(request):
    json_str =request.body
    data = json.loads(json_str)
    username = data['username']
    password = data['password']  
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        try:
            token = Token.objects.get(user=user)
        except Exception:
            token = Token.objects.create(user=user)
        return HttpResponse(token)
    else:
       return HttpResponse('user error')
        

