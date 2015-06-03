from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from django.contrib.contenttypes.models import ContentType
from models import Loginlog
import datetime

def log_addition(self, request, object):
    """
    Log that an object has been successfully added.

    The default implementation creates an admin LogEntry object.
    """
    from django.contrib.admin.models import LogEntry, ADDITION
    LogEntry.objects.log_action(
        user_id         = request.user.pk,
        content_type_id = ContentType.objects.get_for_model(object).pk,
        object_id       = object.pk,
        object_repr     = force_unicode(object),
        action_flag     = ADDITION
    )

def log_change(self, request, object, message):
    """
    Log that an object has been successfully changed.

    The default implementation creates an admin LogEntry object.
    """
    from django.contrib.admin.models import LogEntry, CHANGE
    LogEntry.objects.log_action(
        user_id         = request.user.pk,
        content_type_id = ContentType.objects.get_for_model(object).pk,
        object_id       = object.pk,
        object_repr     = force_unicode(object),
        action_flag     = CHANGE,
        change_message  = message
    )

def log_deletion(self, request, object, object_repr):
    """
    Log that an object will be deleted. Note that this method is called
    before the deletion.

    The default implementation creates an admin LogEntry object.
    """
    from django.contrib.admin.models import LogEntry, DELETION
    LogEntry.objects.log_action(
        user_id         = request.user.id,
        content_type_id = ContentType.objects.get_for_model(self.model).pk,
        object_id       = object.pk,
        object_repr     = object_repr,
        action_flag     = DELETION
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
