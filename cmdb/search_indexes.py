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
    service_name = indexes.CharField()
    department_name = indexes.CharField()
    def get_model(self):
        return HostVirtual
    def index_queryset(self,using=None):
        return self.get_model().objects.all()
    def prepare_department_name(self, obj):
        return obj.department.Department_Name
    def prepare_service_name(self, obj):
        return obj.service.Service_Name

class hostphysicalIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    hostname = indexes.CharField(model_attr='HostName')
    sn = indexes.CharField(model_attr='SN')
    assert_sn = indexes.CharField(model_attr='Asset_SN')
    manage_ip = indexes.CharField(model_attr='Manage_IP')
    rac_ip = indexes.CharField(model_attr='RAC_IP')
    vip = indexes.CharField(model_attr='VIP',null=True)
    nas_ip = indexes.CharField(model_attr='NAS_IP',null=True)
    user = indexes.CharField(model_attr='User',null=True)
    idc_name = indexes.CharField()
    vendor_name = indexes.CharField()
    model_name = indexes.CharField()
    service_name = indexes.CharField()
    department_name = indexes.CharField()
    useinfo = indexes.CharField(model_attr='UseInfo',null=True)
    
    def get_model(self):
        return HostPhysical
    def index_queryset(self,using=None):
        return self.get_model().objects.select_related('Manag_IP').all()
    def prepare_idc_name(self, obj):
        return obj.idc.IDC_Name
    def prepare_vendor_name(self, obj):
        return obj.vendor.Vendor_Name
    def prepare_model_name(self, obj):
        return obj.model.Model_Name
    def prepare_department_name(self, obj):
        return obj.department.Department_Name
    def prepare_service_name(self, obj):
        return obj.service.Service_Name
