#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.admin.models import LogEntry
from cmdb.models import *
import json
import datetime
import urllib

from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

def search(request):
    q = request.GET['q']
    solr_url="http://127.0.0.1:8983/solr/cmdb/select?q=%s&wt=json&indent=true" % q
    query_set =  urllib.urlopen(solr_url.encode('utf-8')).read()
    items = json.loads(query_set)['response']['docs']
    hostphysicals = []
    hostvirtuals = []
    for item in items:
        if 'cmdb.hostphysical' in item['django_ct']:
            hostphysicals.append(item)
        if 'cmdb.hostvirtual' in item['django_ct']:
            hostvirtuals.append(item)
    context = {'hostphysicals':hostphysicals,'hostvirtuals':hostvirtuals}
    return render(request,'search/search.html',context)

    
    
