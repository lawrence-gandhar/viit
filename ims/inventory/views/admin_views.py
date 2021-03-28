"""admin views file."""
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from inventory.models import EmployeeMaster,Device,Location

from inventory.forms import DeviceForm

from collections import defaultdict
from django.contrib import messages

from django.db.models import Q

from inventory.filters import DeviceFilter
# Create your views here.

def employee_obj(request):
    """function to get employee_obj for current logged in user"""
    """ Usage- in case of 'ifm-ldap server and EmployeeMaster table are in consideration. Else use the django user. """
    return (EmployeeMaster.objects.get(user=request.user))

def home(request):
    return render(request,"admin/home.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def ldaps(request):
    allow=[]
    dis=[]
    users = User.objects.all()
    for user in users:
        if user.is_superuser==0:
            if user.is_active:
                allow.append(user.username)
            else:
                dis.append(user.username)

    context={
        'allow':allow,
        'dis':dis
    }
    return render(request,"admin/admin_account.html",context)



def disallow(request):
    if request.method=="POST":
        lis=request.POST.getlist('name')
        print(lis)
        for li in lis:
            u = User.objects.get(username=li)
            u.is_active=0
            u.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])

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
            else:
                print("Failed")
                messages.success(request, 'Device add failed..!!!')
        else:
            print(device_form.errors)

    return  render(request, 'admin/add.html', data)


def allow(request):
    if request.method=="POST":
        lis=request.POST.getlist('name')
        print(lis)
        for li in lis:
            u=User.objects.get(username=li)
            u.is_active=1
            u.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])

#
#
#

def modify_item(request):

    data = defaultdict()

    if request.POST:

        device = Device.objects.get(pk = int(request.POST["device_id"]))
        device_form = DeviceForm(request.POST, instance=device)

        if device_form.is_valid():
            device_form.save()
        else:
            print(device_form.errors)
        return redirect("modify_items")
    else:
        data["items_list"] = Device.objects.filter(Q(allocation_status='Free') | Q(allocation_status__isnull = True) | Q(allocation_status = "-"))
        data["device_form"] = DeviceForm()

    return render(request,'admin/manage_items.html',data)

#
#
#

def search_items(request):
    """Search Items"""
    devices = None
    if 'search' in request.GET.keys():
        args = get_choices_as_per_filters(request.GET)
        device_filter = Device.objects.filter(**args)

    devices = Device.objects.all().order_by('id')
    device_filter = DeviceFilter(request.GET, queryset=devices)

    return render(request,"admin/tabular_view.html", {'filter': device_filter})


def delete(request,allo_id):
    Device.objects.get(pk=allo_id).delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))