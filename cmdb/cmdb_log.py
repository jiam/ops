from django.contrib.admin.models import LogEntry, ADDITION, CHANGE,DELETION
from django.contrib.contenttypes.models import ContentType
from models import *
import datetime

def log_addition(request, object,name,message):
    LogEntry.objects.log_action(
        user_id         = request.user.pk,
        content_type_id = ContentType.objects.get_for_model(object).pk,
        object_id       = object.pk,
        object_repr     = name,
        action_flag     = ADDITION,
        change_message  = message
    )

def log_change(request, object,name, message):
    LogEntry.objects.log_action(
        user_id         = request.user.pk,
        content_type_id = ContentType.objects.get_for_model(object).pk,
        object_id       = object.pk,
        object_repr     = name,
        action_flag     = CHANGE,
        change_message  = message
    )

def log_deletion(request, object,name,message):
    LogEntry.objects.log_action(
        user_id         = request.user.id,
        content_type_id = ContentType.objects.get_for_model(object).pk,
        object_id       = object.pk,
        object_repr     = name,
        action_flag     = DELETION,
        change_message  = message
    )
def log_login(username,result):
    if result == 'ok':
        i= Loginlog(
            user       = username,
            action     = 1,  
            result     = 1,
            message  = 'login sucessed'
        )
        i.save()
    else:
        i = Loginlog(
            user       = username,
            action     = 1,
            result     = 2,
            message  = 'login failed'
        )
        i.save()
def log_logoff(username):
    i= Loginlog(
        user       = username,
        action     = 2,
        result     = 1,
        message  = 'logoff sucessed'
    )
    i.save()
