from haystack import indexes
from cmdb.models import *

class hostvirtualIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    hostname = indexes.CharField(model_attr='HostName')
    manage_ip = indexes.CharField(model_attr='Manage_IP')
    vip = indexes.CharField(model_attr='VIP',null=True)
    nas_ip = indexes.CharField(model_attr='NAS_IP',null=True)
    physical_host_ip = indexes.CharField(model_attr='Physical_Host_IP')
    user = indexes.CharField(model_attr='User',null=True)
    useinfo = indexes.CharField(model_attr='Use_Info',null=True)
    def get_model(self):
        return HostVirtual
    def index_queryset(self,using=None):
        return self.get_model().objects.all()

class hostphysicalIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    hostname = indexes.CharField(model_attr='HostName')
    manage_ip = indexes.CharField(model_attr='Manage_IP')
    rac_ip = indexes.CharField(model_attr='RAC_IP')
    vip = indexes.CharField(model_attr='VIP',null=True)
    nas_ip = indexes.CharField(model_attr='NAS_IP',null=True)
    user = indexes.CharField(model_attr='User',null=True)
    idc_name = indexes.CharField()
    vendor_name = indexes.CharField()
    useinfo = indexes.CharField(model_attr='UseInfo',null=True)
    def get_model(self):
        return HostPhysical
    def index_queryset(self,using=None):
        return self.get_model().objects.select_related().all()
    def prepare_idc_name(self, obj):
        return obj.idc.IDC_Name
    def prepare_vendor_name(self, obj):
        return obj.vendor.Vendor_Name
