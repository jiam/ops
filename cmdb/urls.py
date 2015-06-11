from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import views
import dashboard_views
import object_idc_views
import object_rack_views
import object_vendor_views
import object_cpu_views
import object_memory_views
import object_disk_views
import object_hba_views
import object_pcie_views
import object_nic_views
import object_raid_views
import object_model_views
import object_os_views
import object_kernel_views
import object_service_views
import object_department_views
import object_zone_views
import host_physical_views
import host_virtual_views
import accessories_memory_views
import accessories_disk_views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ops.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$',views.login),
    url(r'^islogin$',views.islogin),
    url(r'^logout$',views.logout),
    url(r'^user$',views.get_user_list),
    url(r'^loginlog/get$',views.get_login_log),
    url(r'^oplog/get$',views.get_op_log),
    url(r'^getuserinfo$',views.get_userinfo),
    url(r'^dashboard/host$',dashboard_views.dashboard_host),
    url(r'^dashboard/os$',dashboard_views.dashboard_os),
    url(r'^object/idc/get$', object_idc_views.idc_get),
    url(r'^object/idc/search$', object_idc_views.idc_search),
    url(r'^object/idc/save$', object_idc_views.idc_save),
    url(r'^object/idc/del$', object_idc_views.idc_del),
    url(r'^object/zone/get$', object_zone_views.zone_get),
    url(r'^object/zone/get/(\d+)$', object_zone_views.zone_get_byid),
    url(r'^object/zone/search$', object_zone_views.zone_search),
    url(r'^object/zone/save$', object_zone_views.zone_save),
    url(r'^object/zone/del$', object_zone_views.zone_del),
    url(r'^object/rack/get$', object_rack_views.rack_get),
    url(r'^object/rack/get/(\d+)$', object_rack_views.rack_get_byid),
    url(r'^object/rack/search$', object_rack_views.rack_search),
    url(r'^object/rack/save$', object_rack_views.rack_save),
    url(r'^object/rack/del$', object_rack_views.rack_del),
    url(r'^object/vendor/get$', object_vendor_views.vendor_get),
    url(r'^object/vendor/search$', object_vendor_views.vendor_search),
    url(r'^object/vendor/save$', object_vendor_views.vendor_save),
    url(r'^object/vendor/del$', object_vendor_views.vendor_del),
    url(r'^object/model/get$', object_model_views.model_get),
    url(r'^object/model/get/(\d+)$', object_model_views.model_get_byid),
    url(r'^object/model/search$', object_model_views.model_search),
    url(r'^object/model/save$', object_model_views.model_save),
    url(r'^object/model/del$', object_model_views.model_del),
    url(r'^object/cpu/get$', object_cpu_views.cpu_get),
    url(r'^object/cpu/search$', object_cpu_views.cpu_search),
    url(r'^object/cpu/save$', object_cpu_views.cpu_save),
    url(r'^object/cpu/del$', object_cpu_views.cpu_del),
    url(r'^object/memory/get$', object_memory_views.memory_get),
    url(r'^object/memory/search$', object_memory_views.memory_search),
    url(r'^object/memory/save$', object_memory_views.memory_save),
    url(r'^object/memory/del$', object_memory_views.memory_del),
    url(r'^object/disk/get$', object_disk_views.disk_get),
    url(r'^object/disk/search$', object_disk_views.disk_search),
    url(r'^object/disk/save$', object_disk_views.disk_save),
    url(r'^object/disk/del$', object_disk_views.disk_del),
    url(r'^object/raid/get$', object_raid_views.raid_get),
    url(r'^object/raid/search$', object_raid_views.raid_search),
    url(r'^object/raid/save$', object_raid_views.raid_save),
    url(r'^object/raid/del$', object_raid_views.raid_del),
    url(r'^object/hba/get$', object_hba_views.hba_get),
    url(r'^object/hba/search$', object_hba_views.hba_search),
    url(r'^object/hba/save$', object_hba_views.hba_save),
    url(r'^object/hba/del$', object_hba_views.hba_del),
    url(r'^object/pcie/get$', object_pcie_views.pcie_get),
    url(r'^object/pcie/search$', object_pcie_views.pcie_search),
    url(r'^object/pcie/save$', object_pcie_views.pcie_save),
    url(r'^object/pcie/del$', object_pcie_views.pcie_del),
    url(r'^object/nic/get$', object_nic_views.nic_get),
    url(r'^object/nic/search$', object_nic_views.nic_search),
    url(r'^object/nic/save$', object_nic_views.nic_save),
    url(r'^object/nic/del$', object_nic_views.nic_del),
    url(r'^object/os/get$', object_os_views.os_get),
    url(r'^object/os/search$', object_os_views.os_search),
    url(r'^object/os/save$', object_os_views.os_save),
    url(r'^object/os/del$', object_os_views.os_del),
    url(r'^object/kernel/get$', object_kernel_views.kernel_get),
    url(r'^object/kernel/search$', object_kernel_views.kernel_search),
    url(r'^object/kernel/save$', object_kernel_views.kernel_save),
    url(r'^object/kernel/del$', object_kernel_views.kernel_del),
    url(r'^object/service/get$', object_service_views.service_get),
    url(r'^object/service/search$', object_service_views.service_search),
    url(r'^object/service/save$', object_service_views.service_save),
    url(r'^object/service/del$', object_service_views.service_del),
    url(r'^object/department/get$', object_department_views.department_get),
    url(r'^object/department/search$', object_department_views.department_search),
    url(r'^object/department/save$', object_department_views.department_save),
    url(r'^object/department/del$', object_department_views.department_del),
    url(r'^host/physical/get$', host_physical_views.physical_get),
    url(r'^host/physical/search$', host_physical_views.physical_search),
    url(r'^host/physical/save$', host_physical_views.physical_save),
    url(r'^host/physical/del$', host_physical_views.physical_del),
    url(r'^host/physical/get/details$', host_physical_views.physical_get_details),
    url(r'^host/virtual/save$', host_virtual_views.virtual_save),
    url(r'^host/virtual/get$', host_virtual_views.virtual_get),
    url(r'^host/virtual/get/details$', host_virtual_views.virtual_get_details),
    url(r'^host/virtual/del$', host_virtual_views.virtual_del),
    url(r'^accessories/memory/save$', accessories_memory_views.memory_save),
    url(r'^accessories/memory/get$', accessories_memory_views.memory_get),
    url(r'^accessories/memory/del$', accessories_memory_views.memory_del),
    url(r'^accessories/disk/save$', accessories_disk_views.disk_save),
    url(r'^accessories/disk/get$', accessories_disk_views.disk_get),
    url(r'^accessories/disk/del$', accessories_disk_views.disk_del),
)
