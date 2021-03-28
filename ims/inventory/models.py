"""moedls.py file."""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.utils import timezone
# Create your models here.

class SubsidiaryMaster(models.Model):
    """ Subsidiary master data model. """

    title = models.CharField(max_length=200)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Subsidiary"

class ProjectMaster(models.Model):
    """ Project master data model. """
    project_status_choices = (
        ('Active', 'Active'),
        ('On_hold', 'On_hold'),
        ('Suspended', 'Suspended'),
        ('Completed', 'Completed'),
    )
    name = models.CharField(max_length=300)
    project_id = models.CharField(max_length=100, unique=True)
    subsidiary = models.ForeignKey(SubsidiaryMaster, on_delete=models.CASCADE)
    project_status = models.CharField(choices=project_status_choices, max_length=20, default='Active')


    def __str__(self):
        return '{}_{}'.format(self.project_id, self.name)

    class Meta:
        verbose_name_plural = 'Project'

class EmployeeMaster(models.Model):
    """ Employee master data model. """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Employee'

class Item_type(models.Model):
    """ Item type data list. """
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Manufacturer(models.Model):
    """ Manufacturer data list. """
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Location(models.Model):
    """ Location  data list. """
    location = models.CharField(max_length=150)

    def __str__(self):
        return self.location

class Device(models.Model):

    """
    Device Details
    """
    iepl_id = models.CharField(db_index=True, blank=False, null=False)

    class Meta(object):
        ordering = ['iepl_id']

    local_admin_choices = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('NA', 'NA'),
    )
    allocation_status_choices = (
        ('Allocated', 'Allocated'),
        ('Decommissioned', 'Decommissioned'),
        ('Free', 'Free'),
    )

    iepl_id = models.CharField(max_length=10, unique=True, verbose_name='iepl_id')
    service_tag = models.CharField(max_length=100, blank = True, null = True)
    item_type = models.ForeignKey(Item_type, on_delete=models.CASCADE, blank = True, null = True)
    host_name = models.CharField(max_length=100, default='NA', blank = True, null = True)
    PO_number = models.CharField(max_length=150, blank = True, null = True)
    PO_date = models.DateTimeField(default=timezone.now, null = True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank = True, null = True)
    model_no = models.CharField(max_length=150, blank = True, null = True)
    project = models.ForeignKey(ProjectMaster, on_delete=models.CASCADE, blank = True, null = True)
    employee = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank = True, null = True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank = True, null = True)
    desk_no = models.CharField(max_length=50, blank = True, null = True)
    local_admin = models.CharField(choices=local_admin_choices, max_length=50, blank = True, null = True)
    asset_code = models.CharField(max_length=100, default='NA', blank = True, null = True)
    CPU = models.CharField(max_length=100, default='NA', blank = True, null = True)
    CPU_speed = models.CharField(max_length=100, default='NA', blank = True, null = True)
    monitor_model = models.CharField(max_length=100, default='NA', blank = True, null = True)
    OS = models.CharField(max_length=100, default='NA', blank = True, null = True)
    RAM = models.CharField(max_length=100, default='NA', blank = True, null = True)
    HDD = models.CharField(max_length=100, default='NA', blank = True, null = True)
    extra_monitor_model = models.CharField(max_length=50, default='NA', blank = True, null = True)
    allocation_status = models.CharField(choices=allocation_status_choices, max_length=20, blank = True, null = True)
    rent = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=100, default='-', blank = True, null = True
                               )

    def __str__(self):
        return self.service_tag

class Allocation(models.Model):

    """
    Allocation Details
    """

    service_tag = models.ForeignKey(Device, on_delete=models.CASCADE)
    allot_to = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return '{}_{}'.format(self.service_tag, self.allot_to)

class Report(models.Model):
    """
    Report Details such as Incorrect assignemnet,Free Item,Return To Store
    """
    report_action_choices = (
        ('Transfer', 'Transfer'),
        ('Incorrect', 'Incorrect'),
        ('Return_store', 'Return_store'),
        ('Free_item', 'Free_item'),
    )
    allocation = models.ForeignKey(Allocation, on_delete=models.CASCADE)
    employee = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE)
    report_action = models.CharField(choices=report_action_choices, max_length=20)

    def __str__(self):
        return '{}_{}'.format(self.report_action, self.employee)

class Service(models.Model):
    """
    Create Service Report
    """
    service_action_choices = (
        ('Release', 'Release'),
        ('Borrow', 'Borrow'),
    )
    service_status_choices = (
        ('Initiated', 'Initiated'),
        ('Completed', 'Completed'),
    )
    service_tag = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE)
    service_action = models.CharField(choices=service_action_choices, max_length=50)
    service_status = models.CharField(choices=service_status_choices, max_length=50, default='Initiated')

    def __str__(self):
        return '{}_{}'.format(self.service_tag, self.employee)


class History_log(models.Model):
    """
    History Log Report
    """
    service_tag = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE)
    date= models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=50,default='--')

    def __str__(self):
        return '{}_{}'.format(self.service_tag, self.employee)

class Logs(models.Model):
    action_time = models.DateTimeField(
        db_index = True
    )

    content = models.TextField(
        blank = True,
        null = True
    )

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        db_index = True
    )
