"""superuser views file."""

from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from inventory.models import Device ,Allocation,Report, Service, History_log
from datetime import datetime
from django.utils import timezone
import pytz
from inventory.filters import DeviceFilter

from django.db.models import Q


from inventory.forms import DeviceForm

from collections import defaultdict
# Create your views here.


def home(request):
    """Super user home feature."""

    objs = Report.objects.all()
    sers = Service.objects.all()
    context={
        'objs':objs,
        'sers':sers
    }
    return render(request,"superuser/home.html",context)


def create(request, allo_id):
    """Create Service Request"""

    sers = Service.objects.get(id=allo_id)
    s= "Create Service"
    context={
        'sers':sers,
        's':s
    }
    return render(request,"superuser/info1.html",context)

def info(request, allo_id):
    """ Information About Report"""
    s = ''
    objs=Report.objects.get(id=allo_id)
    if objs.report_action=='Transfer':
        t=objs.employee.user.username
        s="Transfer to "+t
    elif objs.report_action=='Incorrect':
        s="Incorrect"
    elif objs.report_action=='Return_store':
        s="Return to store"
    elif objs.report_action=='Free_Item':
        s="Free Item"
    context={
        'objs':objs,
        's':s
    }
    return render(request,"superuser/info.html",context)



def accept(request, allo_id):
    """Accept the Report request"""

    objs=Report.objects.get(id=allo_id)
    if objs.report_action=='Transfer':
        IST = pytz.timezone('Asia/Kolkata')
        datetime_ist = datetime.now(IST)
        x=datetime_ist.strftime('%Y:%m:%d %H:%M:%S')
        allo=Allocation.objects.get(service_tag=objs.allocation.service_tag.id)
        allo.delete()
        allo=Allocation(service_tag=objs.allocation.service_tag, employee=objs.employee, date=timezone.now())
        allo.save()
        objs.delete()
        h=History_log(service_tag=objs.allocation.service_tag,employee=objs.employee, date=timezone.now(),
                      status="Allocated")
        h.save()
        messages.success(request,'Request Accepted Successfully !!')
        objs=Report.objects.all()
        sers=Create_service.objects.filter(create_service=1)
        context={
            'objs':objs,
            'sers':sers
        }
        return render(request,"superuser/home.html",context)

    elif objs.report_action == 'Incorrect' or objs.report_action == 'Return_store' or objs.report_action == 'Free_Item':
        IST = pytz.timezone('Asia/Kolkata')
        datetime_ist = datetime.now(IST)
        x=datetime_ist.strftime('%Y:%m:%d %H:%M:%S')
        de=Device.objects.get(iepl_id=objs.allocation.service_tag.iepl_id)
        print(de)
        de.allocation_status=False
        de.save()
        allo=Allocation.objects.get(service_tag=objs.allocation.service_tag.id)
        h=History_log(service_tag=de,employee=objs.employee, date=timezone.now(), status="Free")
        h.save()
        allo.delete()

        objs.delete()
        messages.success(request,'Request Accepted Successfully !!')
        objs=Report.objects.all()
        sers=Service.objects.filter(service_status='Initiated')
        context={
            'objs':objs,
            'sers':sers
        }
        return render(request,"superuser/home.html",context)



def reject(request,allo_id):            # Reject Report request
    objs=Report.objects.get(id=allo_id)
    allo=Allocation.objects.get(service_tag=objs.allocation.service_tag.id)
    allo.comments="Request Rejected"
    allo.save()
    objs.delete()
    messages.success(request,'Request Rejected')
    objs=Report.objects.all()
    sers=Service.objects.filter(service_status='Initiated')
    context={
        'objs':objs,
        'sers':sers
    }
    return render(request,"superuser/home.html",context)


def accept1(request,allo_id):
    """Accept the Create Service request. """

    sers = Service.objects.get(id=allo_id)
    IST = pytz.timezone('Asia/Kolkata')
    datetime_ist = datetime.now(IST)
    x=datetime_ist.strftime('%Y:%m:%d %H:%M:%S')
    if Allocation.objects.filter(service_tag=sers.service_tag): # check for allocation is done or not, if not, then allote
        Allocation.objects.filter(service_tag=sers.service_tag)
        messages.success(request,'Create service Initiated')
        sers.delete()
        objs=Report.objects.all()
        sers=Service.objects.filter(service_status='Initiated')
        context={
            'objs':objs,
            'sers':sers
        }
        return render(request,"superuser/home.html",context)
    else: # create the allocation obj for the service request.
        a=Allocation(service_tag=sers.service_tag,LDAP_ID=sers.LDAP_ID,comments="--",new=1,date=x)
        d=Devices.objects.filter(service_tag=sers.service_tag.service_tag)
        d.update(Allocation_status=1)
        h=History_log(service_tag=sers.service_tag,LDAP_ID=sers.LDAP_ID,date=x,status="Allocated")
        h.save()
        a.save()
        sers.delete()
        messages.success(request,'Request Accepted Successfully !!')
        objs=Report.objects.all()
        sers=Create_service.objects.filter(create_service=1)
        context={
            'objs':objs,
            'sers':sers
        }
        return render(request,"superuser/home.html",context)

def reject1(request,allo_id):
    """Reject the Create Service request. """

    sers = Service.objects.filter(id=allo_id)
    sers.delete()
    messages.success(request,'Request Rejected Successfully !!')
    objs=Report.objects.all()
    sers = Service.objects.filter(service_status='Initiated')
    context={
        'objs':objs,
        'sers':sers
    }
    return render(request,"superuser/home.html",context)


def get_choices_as_per_filters(request_get):
    args = {}

    project = request_get['project']
    if project:
        args['project'] = project

    item_type = request_get['item_type']
    if item_type:
        args['item_type'] = item_type

    manufacturer = request_get['manufacturer']
    if manufacturer:
        args['manufacturer'] = manufacturer

    service_tag = request_get['service_tag']
    if service_tag:
        args['service_tag'] = service_tag

    employee = request_get['employee']
    if employee:
        args['employee'] = employee

    location = request_get['location']
    if location:
        args['location'] = location

    return args

def search_items(request):
    """Search Items"""
    devices = None
    if 'search' in request.GET.keys():
        args = get_choices_as_per_filters(request.GET)
        device_filter = Device.objects.filter(**args)

    devices = Device.objects.all().order_by('id')
    device_filter = DeviceFilter(request.GET, queryset=devices)

    return render(request,"superuser/tabular_view.html", {'filter': device_filter})


def modify_items(request):
    data = defaultdict()

    data = defaultdict()

    if request.POST:

        device = Device.objects.get(pk = int(request.POST["device_id"]))
        device_form = DeviceForm(request.POST, instance=device)

        if device_form.is_valid():
            device_form.save()

            if request.POST["employee"] !="" and request.POST["allocation_status"] == "Allocated":

                employee = User.objects.get(pk = int(request.POST["employee"]))

                ins = Allocation(
                    service_tag = device,
                    allot_to = employee
                )

                ins.save()
        else:
            print(device_form.errors)
        return redirect("edit_item")
    else:
        data["items_list"] = Device.objects.filter(Q(allocation_status='Free') | Q(allocation_status__isnull = True) | Q(allocation_status = "-"))
        data["device_form"] = DeviceForm()

    return render(request, 'superuser/manage_items.html', data)


def add(request):

    data = defaultdict()
    data["device_form"] = DeviceForm()

    if request.POST:

        uniq_id = "iepl000001"

        if Device.objects.exists():
            id = Device.objects.latest('id')
            id = 000000 + id.pk + 1
            id = "{:0>6d}".format(id)
            uniq_id = "iepl" + str(id)

        device_form = DeviceForm(request.POST)
        if device_form.is_valid():
            ins = device_form.save(commit=False)
            if ins:
                ins.iepl_id = uniq_id
                ins.save()
                print("data saved for: ", uniq_id)
                messages.success(request, 'Device added successfully..!!!')
                print(messages)
            else:
                print("Failed")
        else:
            messages.success(request, device_form.errors)
            print(device_form.errors)
    return render(request, 'superuser/add.html', data)




def details(request,allo_id):
    """Information regarding Devices"""

    ids = Device.objects.get(id=allo_id)
    if Allocation.objects.filter(service_tag=ids):
        objs=Allocation.objects.get(service_tag=ids)
        context={
        'objs':objs,
        'ids':ids,
        }
    else:
        context={
        'ids':ids,
        }
    return render(request,"superuser/details.html",context)


def delete(request,allo_id):
    Device.objects.get(pk=allo_id).delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))



def ldap(request):
    """LDAPS Account's """

    allow=[]
    dis=[]
    users = User.objects.all()
    for user in users:
        if user.is_superuser==0 and user.is_staff==0:
            if user.is_active:
                allow.append(user)

            else:
                dis.append(user)

    context={
        'allow':allow,
        'dis':dis
    }
    return render(request,"superuser/ldap.html",context)



def disallow(request):
    """Disallow Account"""
    msg = ''
    if request.method=="POST":
        lis=request.POST.getlist('name')
        print(lis)
        for li in lis:
            u=User.objects.get(username=li)
            u.is_active=0
            u.save()
            msg = 'Added {0} to disallowed user accounts list'.format(u.username)
            messages.success(request, msg)
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])



def allow(request):
    """Allow Accounts"""
    msg = ''
    if request.method=="POST":
        lis=request.POST.getlist('name')
        for li in lis:
            u=User.objects.get(username=li)
            u.is_active=1
            u.save()
            msg = 'Added {0} to Allowed user accounts list'.format(u.username)
            messages.success(request, msg)
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])


def logout(request):
    """logout from session. """

    auth.logout(request)
    return redirect('/')
