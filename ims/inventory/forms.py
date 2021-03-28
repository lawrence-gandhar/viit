"""forms.py file."""

from django.forms import *
from inventory.models import Device

class DeviceForm(ModelForm):
    class Meta:
        allocation_status_choices = (
            ('Allocated', 'Allocated'),
            ('Decommissioned', 'Decommissioned'),
            ('Free', 'Free'),
        )

        model = Device
        fields = ('location', 'service_tag', 'item_type', 'host_name', 'PO_number',
                  'manufacturer', 'model_no', 'project', 'employee', 'location',
                  'desk_no', 'local_admin', 'asset_code', 'CPU', 'CPU_speed', 'monitor_model',
                  'OS', 'RAM', 'HDD', 'extra_monitor_model', 'allocation_status', 'rent',
                  'comment',)


        widgets = {
            'service_tag': TextInput(attrs={'class':'form-control'}),
            'item_type': Select(attrs={'class':'form-control'}),
            'host_name': TextInput(attrs={'class':'form-control'}),
            'PO_number': TextInput(attrs={'class':'form-control'}),
            'manufacturer': Select(attrs={'class':'form-control'}),
            'model_no': TextInput(attrs={'class':'form-control'}),
            'project': Select(attrs={'class':'form-control'}),
            'employee': Select(attrs={'class':'form-control'}),
            'location' : Select(attrs={'class':'form-control'}),
            'desk_no': TextInput(attrs={'class':'form-control'}),
            'local_admin': TextInput(attrs={'class':'form-control'}),
            'asset_code': TextInput(attrs={'class':'form-control'}),
            'CPU': TextInput(attrs={'class':'form-control'}),
            'CPU_speed': TextInput(attrs={'class':'form-control'}),
            'monitor_model': TextInput(attrs={'class':'form-control'}),
            'OS': TextInput(attrs={'class':'form-control'}),
            'RAM': TextInput(attrs={'class':'form-control'}),
            'HDD': TextInput(attrs={'class':'form-control'}),
            'extra_monitor_model': TextInput(attrs={'class':'form-control'}),
            'allocation_status': Select(attrs={'class':'form-control'}, choices = allocation_status_choices),
            'rent':Select(attrs={'class':'form-control'}, choices = ((0, 'No'),(1, 'Yes'))),
            'comment':TextInput(attrs={'class':'form-control'}),
        }
