from django.db import models

# Create your models here.

class Vendor(models.Model):
    Vendor_Name = models.CharField(max_length=30)

class Model(models.Model):
    Model_Name = models.CharField(max_length=30)
    vendor = models.ForeignKey(Vendor)

class OS(models.Model):
    OS_Name = models.CharField(max_length=30)

class Kernel(models.Model):
    Kernel_Name = models.CharField(max_length=30)

class CPU(models.Model):
    CPU_Type = models.CharField(max_length=30)
    CPU_Cores = models.IntegerField()
    CPU_Logical_Cores = models.IntegerField()
    CPU_Frequency = models.CharField(max_length=30)
   

class Memory(models.Model):
    Memory_Type = models.CharField(max_length=30)

class Disk(models.Model):
    Disk_Type = models.CharField(max_length=150)

class HBA(models.Model):
    HBA_Type = models.CharField(max_length=30)
class PCIE(models.Model):
    PCIE_Type = models.CharField(max_length=30)
class NIC(models.Model):
    NIC_Type = models.CharField(max_length=30)

class RAID(models.Model):
    RAID_Type = models.CharField(max_length=100)
    RAID_Cache = models.CharField(max_length=30)
    RAID_Battery = models.CharField(max_length=30)

class Service(models.Model):
    Service_Name = models.CharField(max_length=30)

class IDC(models.Model):
    IDC_Name = models.CharField(max_length=50)
    IDC_Location = models.CharField(max_length=100)
    IDC_Contact = models.CharField(max_length=100)
    IDC_Phone = models.CharField(max_length=20)
    IDC_Email = models.CharField(max_length=50)
    def __unicode__(self):
        return self.IDC_Name

class Rack(models.Model):
    Rack_Name = models.CharField(max_length=30)
    idc = models.ForeignKey(IDC)

class Zone(models.Model):
    Zone_Name = models.CharField(max_length=50)
    idc = models.ForeignKey(IDC)

class IP(models.Model):
    IP = models.IPAddressField()
    IP_Type = models.IntegerField()
    Device_id = models.IntegerField()

class MAC(models.Model):
    MAC = models.CharField(max_length=50)
    MAC_Type = models.IntegerField()
    Device_id = models.IntegerField()

class Department(models.Model):
    Department_Name = models.CharField(max_length=50)
    Department_Contact = models.CharField(max_length=50)
   
class HostPhysical(models.Model):
    SN = models.CharField(max_length=30)
    Asset_SN = models.CharField(max_length=30)
    vendor = models.ForeignKey(Vendor)
    model = models.ForeignKey(Model)
    os = models.ForeignKey(OS,null=True)
    kernel = models.ForeignKey(Kernel)
    HostName = models.CharField(max_length=30)
    service = models.ForeignKey(Service)
    department = models.ForeignKey(Department)
    User = models.CharField(blank=True,null=True,max_length=30)
    UseInfo = models.CharField(blank=True,null=True,max_length=100)
    idc = models.ForeignKey(IDC)
    rack = models.ForeignKey(Rack)
    Rack_Position = models.CharField(max_length=20,blank=True,null=True)
    cpu = models.ForeignKey(CPU)
    CPU_Number = models.IntegerField(blank=True,null=True)
    memory = models.ForeignKey(Memory)
    Memory_Number = models.IntegerField(blank=True,null=True)
    Memory_Size = models.CharField(max_length=20,blank=True,null=True) 
    disk = models.ForeignKey(Disk)
    Disk_Solt_Number = models.IntegerField(blank=True,null=True)
    Disk_Number = models.CharField(max_length=20,blank=True,null=True)
    Disk_Size = models.CharField(max_length=20,blank=True,null=True) 
    hba = models.ForeignKey(HBA)
    HBA_Number = models.IntegerField(blank=True,null=True)
    pcie = models.ForeignKey(PCIE)
    PCIE_Number = models.IntegerField(blank=True,null=True)
    nic = models.ForeignKey(NIC)
    NIC_Number = models.IntegerField(blank=True,null=True)
    raid = models.ForeignKey(RAID)
    RAID_Battery = models.CharField(max_length=30)
    RAID_Level = models.CharField(max_length=30)
    Manage_IP = models.IPAddressField(blank=True,null=True)
    LAN_IP = models.IPAddressField(blank=True,null=True)
    WAN_IP = models.IPAddressField(blank=True,null=True)
    RAC_IP = models.IPAddressField(blank=True,null=True)
    NAS_IP = models.IPAddressField(blank=True,null=True)
    VIP = models.IPAddressField(blank=True,null=True)
    WAN_mac = models.CharField(max_length=20,blank=True,null=True)
    LAN_mac = models.CharField(max_length=20,blank=True,null=True)
    RAC_mac = models.CharField(max_length=20,blank=True,null=True)
    Purchasing_Time = models.DateField(blank=True,null=True)
    Guarantee_Time = models.DateField(blank=True,null=True)
    Change_Time = models.DateField(blank=True,null=True)
    Change_Info = models.CharField(blank=True,null=True,max_length=100)
    Up_Time = models.DateField(blank=True,null=True)
    Status = models.IntegerField(blank=True,null=True)
    Remarks =  models.CharField(blank=True,null=True,max_length=100)
    zone = models.ForeignKey(Zone)


class HostVirtual(models.Model):
    os = models.ForeignKey(OS,null=True)
    kernel = models.ForeignKey(Kernel)
    HostName = models.CharField(max_length=30)
    service = models.ForeignKey(Service)
    User = models.CharField(blank=True,null=True,max_length=30)
    department = models.ForeignKey(Department)
    vCPU_Number = models.IntegerField(blank=True,null=True)
    Memory_Size = models.CharField(max_length=20,blank=True,null=True)
    Disk_Size = models.CharField(max_length=20,blank=True,null=True)
    Manage_IP = models.IPAddressField(blank=True,null=True)
    NAS_IP = models.IPAddressField(blank=True,null=True)
    VIP = models.IPAddressField(blank=True,null=True)
    SSH_Port = models.IntegerField(blank=True,null=True)
    LAN_IP = models.IPAddressField(blank=True,null=True)
    WAN_IP = models.IPAddressField(blank=True,null=True)
    Physical_Host_IP = models.IPAddressField(blank=True,null=True)
    WAN_mac = models.CharField(max_length=20,blank=True,null=True)
    LAN_mac = models.CharField(max_length=20,blank=True,null=True)
    RAC_mac = models.CharField(max_length=20,blank=True,null=True)
    Application_Time = models.DateField(blank=True,null=True) 
    Change_Time = models.DateField(blank=True,null=True)
    Change_Info = models.CharField(blank=True,null=True,max_length=100)
    Use_Info = models.CharField(blank=True,null=True,max_length=100)
    Use_Period = models.CharField(blank=True,null=True,max_length=100)
    Deploy_Path = models.CharField(blank=True,null=True,max_length=60)
    Up_Time = models.DateField(blank=True,null=True)
    Status = models.IntegerField(blank=True,null=True)
    Remarks =  models.CharField(blank=True,null=True,max_length=100)


class Loginlog(models.Model):
    action_time = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=30)
    action = models.IntegerField()
    result = models.IntegerField()
    message = models.CharField(blank=True,null=True,max_length=100)


class Accessories_Memory(models.Model):
    SN = models.CharField(max_length=30)
    Memory_Type = models.ForeignKey(Memory) 
    Status = models.IntegerField(blank=True,null=True)
    Host_IP =  models.IPAddressField(blank=True,null=True)
class Accessories_Disk(models.Model):
    SN = models.CharField(max_length=30)
    Disk_Type = models.ForeignKey(Disk) 
    Status = models.IntegerField(blank=True,null=True)
    Host_IP =  models.IPAddressField(blank=True,null=True)
