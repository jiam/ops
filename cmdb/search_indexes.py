from haystack import indexes
from cmdb.models import *

class hostvirtualIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    hostname = indexes.CharField(model_attr='HostName')
    manage_ip = indexes.CharField(model_attr='Manage_IP')
    physical_host_ip = indexes.CharField(model_attr='Physical_Host_IP')
    user = indexes.CharField(model_attr='User',null=True)
    def get_model(self):
        return HostVirtual
    def index_queryset(self,using=None):
        return self.get_model().objects.all()

class hostphysicalIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    hostname = indexes.CharField(model_attr='HostName')
    manage_ip = indexes.CharField(model_attr='Manage_IP')
    user = indexes.CharField(model_attr='User',null=True)
    def get_model(self):
        return HostPhysical
    def index_queryset(self,using=None):
        return self.get_model().objects.all()
