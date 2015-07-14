from rest_framework.authtoken.models import Token
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from cmdb.models import *
from django.contrib.auth.models import User
from django.core  import serializers
import json
import cmdb_log
import urllib

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
        idcs = list(IDC.objects.all().values())
        result ={'result':idcs}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    

@csrf_exempt
def get_vendor(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        vendors = list(Vendor.objects.all().values())
        result ={'result':vendors}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    


@csrf_exempt
def get_model(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        if 'params' in data:
            vendor_id = data['params']['vendor_id']
            models = list(Model.objects.filter(vendor=vendor_id).values())
        else:
            models = list(Model.objects.all().values())
        result ={'result':models}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    

@csrf_exempt
def get_os(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        oss = list(OS.objects.all().values())
        result ={'result':oss}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    

@csrf_exempt
def get_kernel(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        kernels = list(Kernel.objects.all().values())
        result ={'result':kernels}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    

@csrf_exempt
def get_department(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        departments = list(Department.objects.all().values())
        result ={'result':departments}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    

@csrf_exempt
def get_service(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        services = list(Service.objects.all().values())
        result ={'result':services}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    


@csrf_exempt
def get_zone(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        if 'params' in data:
            idc_id = data['params']['idc_id']
            models = list(Zone.objects.filter(idc=idc_id).values())
        else:
            models = list(Zone.objects.all().values())
        result ={'result':models}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    

@csrf_exempt
def get_rack(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        if 'params' in data:
            idc_id = data['params']['idc_id']
            models = list(Rack.objects.filter(idc=idc_id).values())
        else:
            models = list(Rack.objects.all().values())
        result ={'result':models}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    

@csrf_exempt
def get_cpu(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        cpus = list(CPU.objects.all().values())
        result ={'result':cpus}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    


@csrf_exempt
def get_disk(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        disks = list(Disk.objects.all().values())
        result ={'result':disks}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    


@csrf_exempt
def get_memory(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        memorys = list(Memory.objects.all().values())
        result ={'result':memorys}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    


@csrf_exempt
def get_raid(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        raids = list(RAID.objects.all().values())
        result ={'result':raids}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    

@csrf_exempt
def get_hba(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        hbas = list(HBA.objects.all().values())
        result ={'result':hbas}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    

@csrf_exempt
def get_pcie(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        pcies = list(PCIE.objects.all().values())
        result ={'result':pcies}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    


@csrf_exempt
def get_nic(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token'] 
    try:
        result = Token.objects.get(key=token)
        nics = list(NIC.objects.all().values())
        result ={'result':nics}
        response = json.dumps(result)
        return HttpResponse(response)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)    

@csrf_exempt
def host_physical_add(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token']
    try:
        result = Token.objects.get(key=token)
        user_id = result.user_id
        request.user = User.objects.get(id=user_id)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)
    try:
        params = data['params']
        params['vendor'] = Vendor.objects.get(id=params['vendor'])
        params['model'] = Model.objects.get(id=params['model'])
        params['os'] = OS.objects.get(id=params['os'])
        params['kernel'] = Kernel.objects.get(id=params['kernel'])
        params['service'] = Service.objects.get(id=params['service'])
        params['department'] = Department.objects.get(id=params['department'])
        params['idc'] = IDC.objects.get(id=params['idc'])
        params['rack'] = Rack.objects.get(id=params['rack'])
        params['cpu'] = CPU.objects.get(id=params['cpu'])
        params['memory'] = Memory.objects.get(id=params['memory'])
        params['disk'] = Disk.objects.get(id=params['disk'])
        params['hba'] = HBA.objects.get(id=params['hba'])
        params['pcie'] = PCIE.objects.get(id=params['pcie'])
        params['nic'] = NIC.objects.get(id=params['nic'])
        params['raid'] = RAID.objects.get(id=params['raid'])
        params['zone'] = Zone.objects.get(id=params['zone'])
        host = HostPhysical(**params)
        host.save()
        cmdb_log.log_addition(request,host,params['Manage_IP'],params)
        result = {'result':{'status':1,'info':'physical host add sucesses'}}
        response = json.dumps(result)
        return HttpResponse(response)
    except Exception,e:
        result = {'result':{'status':0,'info':str(e)}}
        response = json.dumps(result)
        return HttpResponse(response)
        
    
@csrf_exempt
def host_physical_update(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token']
    try:
        result = Token.objects.get(key=token)
        user_id = result.user_id
        request.user = User.objects.get(id=user_id)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)
    try:
        params = data['params']
        id = params.pop('id')
        host = HostPhysical.objects.filter(id=id)
        if 'vendor' in params:
            params['vendor'] = Vendor.objects.get(id=params['vendor'])
        if 'model' in params:
            params['model'] = Model.objects.get(id=params['model'])
        if 'os' in params:
            params['os'] = OS.objects.get(id=params['os'])
        if 'kernel' in params:
            params['kernel'] = Kernel.objects.get(id=params['kernel'])
        if 'service' in params:
            params['service'] = Service.objects.get(id=params['service'])
        if 'department' in params:
            params['department'] = Department.objects.get(id=params['department'])
        if 'idc' in params:
            params['idc'] = IDC.objects.get(id=params['idc'])
        if 'rack' in params: 
            params['rack'] = Rack.objects.get(id=params['rack'])
        if 'cpu' in params:
            params['cpu'] = CPU.objects.get(id=params['cpu'])
        if 'memory' in params:
            params['memory'] = Memory.objects.get(id=params['memory'])
        if 'disk' in params:
            params['disk'] = Disk.objects.get(id=params['disk'])
        if 'hba' in params:
            params['hba'] = HBA.objects.get(id=params['hba'])
        if 'pcie' in params:
            params['pcie'] = PCIE.objects.get(id=params['pcie'])
        if 'nic' in params:
            params['nic'] = NIC.objects.get(id=params['nic'])
        if 'raid' in params:
            params['raid'] = RAID.objects.get(id=params['raid'])
        if 'zone' in params:
            params['zone'] = Zone.objects.get(id=params['zone'])
        host.update(**params)
        cmdb_log.log_change(request,host[0],host[0].Manage_IP,params)
        result = {'result':{'status':1,'info':'physical host update sucesses'}}
        response = json.dumps(result)
        return HttpResponse(response)
    except Exception,e:
        result = {'result':{'status':0,'info':str(e)}}
        response = json.dumps(result)
        return HttpResponse(response)
        

@csrf_exempt
def host_physical_get(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token']
    try:
        result = Token.objects.get(key=token)
        user_id = result.user_id
        request.user = User.objects.get(id=user_id)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)
    try:
        if 'params' in data:
            params = data['params']
            physicals = HostPhysical.objects.select_related('Manage_IP').filter(**params).order_by('Manage_IP')
            total = physicals.count()
            physicals = serializers.serialize("json",physicals,use_natural_keys=True)
            response = '{"result":{"total":%s,"data":%s}}' % (total,physicals)
            return HttpResponse(response)
        else:
            physicals = HostPhysical.objects.select_related('Manage_IP').all().order_by('Manage_IP')
            total = physicals.count()
            physicals = serializers.serialize("json",physicals,use_natural_keys=True)
            response = '{"result":{"total":%s,"data":%s}}' % (total,physicals)
            return HttpResponse(response)
            
    except Exception,e:
        result = {'result':{'status':0,'info':str(e)}}
        response = json.dumps(result)
        return HttpResponse(response)
        

@csrf_exempt
def host_virtual_add(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token']
    try:
        result = Token.objects.get(key=token)
        user_id = result.user_id
        request.user = User.objects.get(id=user_id)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)
    try:
        params = data['params']
        params['os'] = OS.objects.get(id=params['os'])
        params['kernel'] = Kernel.objects.get(id=params['kernel'])
        params['service'] = Service.objects.get(id=params['service'])
        params['department'] = Department.objects.get(id=params['department'])
        host = HostVirtual(**params)
        host.save()
        cmdb_log.log_addition(request,host,params['Manage_IP'],params)
        result = {'result':{'status':1,'info':'virtual host add sucesses'}}
        response = json.dumps(result)
        return HttpResponse(response)
    except Exception,e:
        result = {'result':{'status':0,'info':str(e)}}
        response = json.dumps(result)
        return HttpResponse(response)



@csrf_exempt
def host_virtual_update(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token']
    try:
        result = Token.objects.get(key=token)
        user_id = result.user_id
        request.user = User.objects.get(id=user_id)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)
    try:
        params = data['params']
        id = params.pop('id')
        host = HostVirtual.objects.filter(id=id)
        if 'os' in params:
            params['os'] = OS.objects.get(id=params['os'])
        if 'kernel' in params:
            params['kernel'] = Kernel.objects.get(id=params['kernel'])
        if 'service' in params:
            params['service'] = Service.objects.get(id=params['service'])
        if 'department' in params:
            params['department'] = Department.objects.get(id=params['department'])
        host.update(**params)
        cmdb_log.log_change(request,host[0],host[0].Manage_IP,params)
        result = {'result':{'status':1,'info':'virtual host update sucesses'}}
        response = json.dumps(result)
        return HttpResponse(response)
    except Exception,e:
        result = {'result':{'status':0,'info':str(e)}}
        response = json.dumps(result)
        return HttpResponse(response)


@csrf_exempt
def host_virtual_get(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token']
    try:
        result = Token.objects.get(key=token)
        user_id = result.user_id
        request.user = User.objects.get(id=user_id)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)
    try:
        if 'params' in data:
            params = data['params']
            virtuals = HostVirtual.objects.select_related('Manage_IP').filter(**params).order_by('Manage_IP')
            total = virtuals.count()
            physicals = serializers.serialize("json",virtuals,use_natural_keys=True)
            response = '{"result":{"total":%s,"data":%s}}' % (total,physicals)
            return HttpResponse(response)
        else:
            virtuals = HostVirtual.objects.select_related('Manage_IP').all().order_by('Manage_IP')
            total = virtuals.count()
            virtuals = serializers.serialize("json",virtuals,use_natural_keys=True)
            response = '{"result":{"total":%s,"data":%s}}' % (total,virtuals)
            return HttpResponse(response)
            
    except Exception,e:
        result = {'result':{'status':0,'info':str(e)}}


@csrf_exempt
def search(request):
    json_str = request.body
    data = json.loads(json_str)
    token = data['token']
    try:
        result = Token.objects.get(key=token)
        user_id = result.user_id
        request.user = User.objects.get(id=user_id)
    except Token.DoesNotExist:
        result = {'result':'auth failed'}
        response = json.dumps(result)
        return HttpResponse(response)
    q = data['params'] 
    solr_url="http://127.0.0.1:8983/solr/cmdb/select?q=" + urllib.quote(q.encode('utf-8')) + "&wt=json&indent=true"
    query_set =  urllib.urlopen(solr_url).read()
    #items = json.loads(query_set)
    return HttpResponse(query_set)
