"""user views file."""

from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from inventory.models import Device, Allocation, Report, Service, History_log, EmployeeMaster, ProjectMaster, Location,Item_type, Manufacturer
from django.db import connection
from django import template

from inventory.filters import *
# Create your views here.


def employee_obj(request):
    """function to get employee_obj for current logged in user"""
    """ Usage- in case of 'ifm-ldap server and EmployeeMaster table are in consideration. Else use the django user. """
    return (EmployeeMaster.objects.get(user=request.user))

def home(request):
    """View function for user-home page feature."""

    user_id = request.user
    objs = Allocation.objects.filter(allot_to=user_id).all()
    context={
        'objs':objs
        }
    return render(request,"user/home.html",context)

def Information(request, allo_id):
    """ Information about Devices """

    objs=Allocation.objects.get(id=allo_id)
    users = EmployeeMaster.objects.all()  # change the Employee master to User in case of django user model usage.
    # if objs.new:
    #     objs.new=0
    #     objs.save()
    #
    if Report.objects.filter(allocation=allo_id):
        r=Report.objects.get(allocation=allo_id)
    else:
        r=Report.objects.filter(allocation=allo_id)
    cnt=Report.objects.filter(allocation=objs).count()
    context={
        'objs':objs,
        'r':r,
        'cnt':cnt,
        'users':users
        }
    return render(request,"user/Information.html",context)

def incorrect(request, allo_id):
    """ Incorrect item  Assignment """

    ids=Allocation.objects.get(id=allo_id)
    cnt=Report.objects.filter(allocation=ids).count()
    if cnt==0:
        # r=Report(allocation=ids,Transfer=0,Incorrect=1,Return_store=0,Free_Item=0,to_user="--")
        r=Report(allocation=ids, report_action='Incorrect', employee=employee_obj(request))
        print(r)
        r.save()
        messages.success(request,'Your Request of Incorrect Item is send to Superuser')
        return redirect(request.META['HTTP_REFERER'])
    else:
        try:
            Report.objects.get(allocation=ids, report_action='Free_item')
            messages.error(request,'Please Wait Your Freeing this item request is pending')
            return redirect(request.META['HTTP_REFERER'])
        except:
            try:
                Report.objects.get(allocation=ids, report_action='Incorrect')
                messages.error(request,'Please Wait Your Incorrect item request is pending')
                return redirect(request.META['HTTP_REFERER'])
            except:
                try:
                    Report.objects.get(allocation=ids, report_action='Return_store')
                    messages.error(request,'Please Wait Your Return to Store this item request is pending')
                    return redirect(request.META['HTTP_REFERER'])
                except:
                    Report.objects.get(allocation=ids, report_action='Transfer')
                    messages.error(request,'Please Wait Your Transfering this item request is pending')
                    return redirect(request.META['HTTP_REFERER'])

def Return_to_store(request,allo_id):  
    ids=Allocation.objects.get(id=allo_id)
    cnt=Report.objects.filter(allocation=ids).count()
    print(cnt)
    if cnt==0:
        r=Report(allocation=ids, report_action='Return_store', employee=employee_obj(request))
        r.save()
        messages.success(request,'Your Request of Returning Item is send to Superuser')
        return redirect(request.META['HTTP_REFERER'])
    else:
        try:
            Report.objects.get(allocation=ids, report_action='Free_item')
            messages.error(request, 'Please Wait Your Freeing this item request is pending')
            return redirect(request.META['HTTP_REFERER'])
        except:
            try:
                Report.objects.get(allocation=ids, report_action='Incorrect')
                messages.error(request, 'Please Wait Your Incorrect item request is pending')
                return redirect(request.META['HTTP_REFERER'])
            except:
                try:
                    Report.objects.get(allocation=ids, report_action='Return_store')
                    messages.error(request, 'Please Wait Your Return to Store this item request is pending')
                    return redirect(request.META['HTTP_REFERER'])
                except:
                    Report.objects.get(allocation=ids, report_action='Transfer')
                    messages.error(request, 'Please Wait Your Transfering this item request is pending')
                    return redirect(request.META['HTTP_REFERER'])

def Free_Item(request,allo_id):
    """Free item feature for user - home page."""

    ids=Allocation.objects.get(id=allo_id)
    cnt=Report.objects.filter(allocation=ids).count()
    print(cnt)
    if cnt== 0:
        r=Report(allocation=ids, report_action='Free_item', employee=employee_obj(request))
        user=ids.employee.user
        r.save()
        txt='Your Request of Freeing this Item is send to '+user
        messages.success(request,txt)
        return redirect(request.META['HTTP_REFERER'])
    else:
        try:
            Report.objects.get(allocation=ids, report_action='Free_item')
            messages.error(request, 'Please Wait Your Freeing this item request is pending')
            return redirect(request.META['HTTP_REFERER'])
        except:
            try:
                Report.objects.get(allocation=ids, report_action='Incorrect')
                messages.error(request, 'Please Wait Your Incorrect item request is pending')
                return redirect(request.META['HTTP_REFERER'])
            except:
                try:
                    Report.objects.get(allocation=ids, report_action='Return_store')
                    messages.error(request, 'Please Wait Your Return to Store this item request is pending')
                    return redirect(request.META['HTTP_REFERER'])
                except:
                    Report.objects.get(allocation=ids, report_action='Transfer')
                    messages.error(request, 'Please Wait Your Transfering this item request is pending')
                    return redirect(request.META['HTTP_REFERER'])

def Transfer(request,allo_id):
    """Transfer item feature."""

    if request.method=="POST":
        id1=request.POST.get('mySelect', None)
        ids=Allocation.objects.get(id=allo_id)
        cnt=Report.objects.filter(allocation=ids).count()
        print(id1)
        if cnt == 0:
            r=Report(allocation=ids, report_action='Transfer', employee = employee_obj(request))
            r.save()
            mess="Trasfer Request to " + id1 + " is sent to Superuser"
            messages.success(request,mess)
            return redirect(request.META['HTTP_REFERER'])
        else:
            try:
                Report.objects.get(allocation=ids, report_action='Free_item')
                messages.error(request, 'Please Wait Your Freeing this item request is pending')
                return redirect(request.META['HTTP_REFERER'])
            except:
                try:
                    Report.objects.get(allocation=ids, report_action='Incorrect')
                    messages.error(request, 'Please Wait Your Incorrect item request is pending')
                    return redirect(request.META['HTTP_REFERER'])
                except:
                    try:
                        Report.objects.get(allocation=ids, report_action='Return_store')
                        messages.error(request, 'Please Wait Your Return to Store this item request is pending')
                        return redirect(request.META['HTTP_REFERER'])
                    except:
                        Report.objects.get(allocation=ids, report_action='Transfer')
                        messages.error(request, 'Please Wait Your Transfering this item request is pending')
                        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])

def search(request):
    """Search a Particular items Based upon specific filters"""

    if request.method=='POST':
        location=request.POST.get('location')
        pc=request.POST.get('pc')
        allo=request.POST.get('Allocated')
        free=request.POST.get('Free')
        Dicommissioned=request.POST.get('Dicommissioned')


        if allo=="on":
            allo=1
        if free=="on" or allo==None:
            allo=0

        if Dicommissioned=="on":
            Dicommissioned=1
        else:
            Dicommissioned=0
        
        if location=="Any":
            if pc=="Any":
                objs=Device.objects.filter(allocation_status='Allocated')
            else:
                objs=Device.objects.filter(item_type=pc,allocation_status='Allocated')
        elif pc=="Any":
            objs=Device.objects.filter(location__location=str(location),allocation_status='Allocated')
        else:

            objs=Device.objects.filter(location__location=str(location),item_type=pc,allocation_status='Allocated')

        context={
        'objs':objs,
        }
        if objs.exists():
            return render(request,"user/search.html",context)
        else:
            messages.error(request,'No Such Item Exists')
            return render(request,"user/search.html",context)

    else:
        return render(request,"user/search.html")

def details(request, allo_id):
    """Details of Devices after the searched item."""

    ids=Devices.objects.get(service_tag=allo_id)
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
    return render(request,"user/details.html",context)

def create_service(request, allo_id):
    """Create Service Request """

    #ids=Allocation.objects.filter(id=allo_id)
    objs = Device.objects.get(service_tag=allo_id)
    cnt=0
    if Service.objects.filter(service_tag=objs):
        cnt = Service.objects.filter(service_tag=objs).count()

    if cnt==0:
        c = Service(service_tag=objs, employee=employee_obj(request))
        c.save()
        messages.success(request,'Your Request of Service Item is send to Superuser')
        return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request,'Please Wait Your/Another user\'s request is pending')
        return redirect(request.META['HTTP_REFERER'])
    
def release(request,allo_id):
    """Relesed Request function"""

    objs=Devices.objects.get(service_tag=allo_id)
    username=request.user.get_username()
    cnt=Create_service.objects.filter(service_tag=objs).count()
    comments="Release request from "+username
    if cnt==0:
        c=Create_service(service_tag=objs,release=1,LDAP_ID=username)
        c.save()
        Allocation.objects.filter(service_tag=objs).update(comments=comments)
        messages.success(request,'Your Request of releasing Item is send to Superuser')
        return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request,'Please Wait Your/Another user\'s request is pending')
        return redirect(request.META['HTTP_REFERER'])


def borrow(request,allo_id):
    objs=Devices.objects.get(service_tag=allo_id)
    u=Allocation.objects.get(service_tag=objs)
    username=request.user.get_username()
    cnt=Create_service.objects.filter(service_tag=objs).count()
    comments="Borrow request from "+username
    if cnt==0:
        c=Create_service(service_tag=objs,borrow=1,LDAP_ID=username)
        c.save()
        Allocation.objects.filter(service_tag=objs).update(comments=comments)
        messages.success(request,'Your Request of borrowing Item is send to Superuser')
        return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request,'Please Wait Your/Another user\'s request is pending')
        return redirect(request.META['HTTP_REFERER'])


def projectlist(request):
    """Project list feature"""
    title = ''
    if request.method=='POST':
        labels = []
        data = []
        s=[]
        c=[]
        projs = ProjectMaster.objects.all()
        s.append("Active")
        s.append("Completed")
        s.append("Suspended")
        c.append(ProjectMaster.objects.filter(project_status="Active").count())
        c.append(ProjectMaster.objects.filter(project_status="Completed").count())
        c.append(ProjectMaster.objects.filter(project_status="Suspended").count())
        for proj in projs:
            labels.append(proj.name)
            cnt = Allocation.objects.filter(service_tag__project__project_id=str(proj.project_id)).count()
            data.append(cnt)
        status=request.POST.get('status')
        objs=ProjectMaster.objects.all()
        if status=="All":
            objs=ProjectMaster.objects.all()
            title = 'For All Projects'
        elif status=='Active':
            objs=ProjectMaster.objects.filter(project_status='Active')
            title = 'For Active Projects'
        elif status=='Suspended':
            objs=ProjectMaster.objects.filter(project_status='Suspended')
            title = 'For Suspended Projects'
        else:
            objs=ProjectMaster.objects.filter(project_status='Completed')
            title = 'For Completed Projects'
        context={
            'objs':objs,
                }
        if objs.exists():
            context={
            'labels':labels,
            'data':data,
            's':s,
            'c':c,
            'objs':objs,
            'title': title,
        }
            return render(request,"user/projectlist.html",context)
        else:
            context={
            'labels':labels,
            'data':data,
            's':s,
            'c':c
        }
            messages.error(request,'No Such Item Exists')
            return render(request,"user/projectlist.html",context)

    else:
        labels = []
        data = []
        s=[]
        c=[]
        objs = ProjectMaster.objects.all()
        s.append("Active")
        s.append("Completed")
        s.append("Suspended")
        c.append(ProjectMaster.objects.filter(project_status="Active").count())
        c.append(ProjectMaster.objects.filter(project_status="Completed").count())
        c.append(ProjectMaster.objects.filter(project_status="Suspended").count())
        for proj in objs:
            labels.append(proj.name)
            cnt=Allocation.objects.filter(service_tag__project__project_id=str(proj.project_id)).count()
            data.append(cnt)

        context={
            'labels':labels,
            'data':data,
            's':s,
            'c':c,
            'objs':objs,
            'title':'For All Projects',
        }
    return render(request,"user/projectlist.html",context)



def project_info(request, allo_id):
    """ project info feature."""

    objs=ProjectMaster.objects.get(id=allo_id)
    cnt=Allocation.objects.filter(service_tag__project__project_id=allo_id).count()
    context={
        'objs':objs,
        'cnt':cnt
    }
    return render(request,"user/projectinfo.html",context)


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

def advance(request):
    """Advance Filtering Function"""

    devices = None
    if 'search' in request.GET.keys():
        args = get_choices_as_per_filters(request.GET)
        device_filter = Device.objects.filter(**args)

    devices = Device.objects.all()
    device_filter = DeviceFilter(request.GET, queryset=devices)
        # return render(request, "user/advance.html")

    return render(request, "user/advance.html", {'filter': device_filter })

def search_items(request):
    """Advance Filtering Function"""

    devices = None
    if 'search' in request.GET.keys():
        args = get_choices_as_per_filters(request.GET)
        device_filter = Device.objects.filter(**args)

    devices = Device.objects.all()
    device_filter = DeviceFilter(request.GET, queryset=devices)
        # return render(request, "user/advance.html")

    return render(request, "user/tabular_view.html", {'filter': device_filter })



def tp(request,allo_id):                        # Information of devices after the advance filtering
    objs = request.session.get('objs', None)
    total = request.session.get('total', None)
    cnt = request.session.get('cnt', None)
    query = request.session.get('query', None)
    users=User.objects.all()
    print(allo_id)
    objss=Devices.objects.get(uniq_id=allo_id)
    hists=History_log.objects.none()
    if History_log.objects.filter(service_tag=objss):
        hists=History_log.objects.filter(service_tag=objss)
    if Allocation.objects.filter(service_tag=objss):
        ids=Allocation.objects.get(service_tag=objss)
        context={
        'objss':objss,
        'objs':objs,
        'query':query,
        'ids':ids,
        'users':users,
        'cnt':cnt,
        'total':total,
        'hists':hists      
    }
    else:
        context={
        'objss':objss,
        'objs':objs,
        'query':query,   
        'cnt':cnt,
        'total':total,
        'hists':hists  
    }
    t=template.loader.get_template('user/advance.html')
    
    return HttpResponse(t.render(context,request))

def service(request):
    """ Multiple report function """

    username=request.user.get_username()
    lis=[]
    objs=Allocation.objects.filter(allot_to=employee_obj(request)).all()
    req=Report.objects.filter().all()
    for obj in objs:
        if  Report.objects.filter(allocation=obj):
            continue
        else:
            lis.append(obj)


    context={
        'lis':lis,
        'req':req
        }
    return render(request,"user/service.html",context)


def incorrect1(request):
    """Multiple Incorrect Items"""

    if request.method=="POST":
        li=request.POST.getlist('allocation_id')
        print(li)
        for id in li:
            # response = incorrect(request, id)
            ids = Allocation.objects.get(id=id)
            cnt = Report.objects.filter(allocation=ids).count()
            if cnt == 0:
                # r=Report(allocation=ids,Transfer=0,Incorrect=1,Return_store=0,Free_Item=0,to_user="--")
                r = Report(allocation=ids, report_action='Incorrect', employee=employee_obj(request))
                print(r)
                r.save()
                messages.success(request, 'Your Request of Incorrect Item is send to Superuser')
                return redirect(request.META['HTTP_REFERER'])
            else:
                try:
                    Report.objects.get(allocation=ids, report_action='Free_item')
                    messages.error(request, 'Please Wait Your Freeing this item request is pending')
                    return redirect(request.META['HTTP_REFERER'])
                except:
                    try:
                        Report.objects.get(allocation=ids, report_action='Incorrect')
                        messages.error(request, 'Please Wait Your Incorrect item request is pending')
                        return redirect(request.META['HTTP_REFERER'])
                    except:
                        try:
                            Report.objects.get(allocation=ids, report_action='Return_store')
                            messages.error(request, 'Please Wait Your Return to Store this item request is pending')
                            return redirect(request.META['HTTP_REFERER'])
                        except:
                            Report.objects.get(allocation=ids, report_action='Transfer')
                            messages.error(request, 'Please Wait Your Transfering this item request is pending')
                            return redirect(request.META['HTTP_REFERER'])

        return render(request, "user/service.html")
    else:
        return render(request, "user/service.html")


def Free_Item1(request):            # Multiple Free Item
    if request.method=="POST":
        li=request.POST.getlist('allocation_id')
        for id in li:
            ids = Allocation.objects.get(id=id)
            cnt = Report.objects.filter(allocation=ids).count()
            print(cnt)
            if cnt == 0:
                r = Report(allocation=ids, report_action='Free_item', employee=employee_obj(request))
                user = ids.allot_to.user
                r.save()
                txt = 'Your Request of Freeing this Item is send to ' + user.username
                messages.success(request, txt)
                return redirect(request.META['HTTP_REFERER'])
            else:
                try:
                    Report.objects.get(allocation=ids, report_action='Free_item')
                    messages.error(request, 'Please Wait Your Freeing this item request is pending')
                    return redirect(request.META['HTTP_REFERER'])
                except:
                    try:
                        Report.objects.get(allocation=ids, report_action='Incorrect')
                        messages.error(request, 'Please Wait Your Incorrect item request is pending')
                        return redirect(request.META['HTTP_REFERER'])
                    except:
                        try:
                            Report.objects.get(allocation=ids, report_action='Return_store')
                            messages.error(request, 'Please Wait Your Return to Store this item request is pending')
                            return redirect(request.META['HTTP_REFERER'])
                        except:
                            Report.objects.get(allocation=ids, report_action='Transfer')
                            messages.error(request, 'Please Wait Your Transfering this item request is pending')
                            return redirect(request.META['HTTP_REFERER'])

        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])

def Return_to_store1(request):
    """Multiple Return to store"""

    if request.method=="POST":
        li=request.POST.getlist('allocation_id')
        for id in li:
            ids = Allocation.objects.get(id=id)
            cnt = Report.objects.filter(allocation=ids).count()
            print(cnt)
            if cnt == 0:
                r = Report(allocation=ids, report_action='Return_store', employee=employee_obj(request))
                r.save()
                messages.success(request, 'Your Request of Returning Item is send to Superuser')
                return redirect(request.META['HTTP_REFERER'])
            else:
                try:
                    Report.objects.get(allocation=ids, report_action='Free_item')
                    messages.error(request, 'Please Wait Your Freeing this item request is pending')
                    return redirect(request.META['HTTP_REFERER'])
                except:
                    try:
                        Report.objects.get(allocation=ids, report_action='Incorrect')
                        messages.error(request, 'Please Wait Your Incorrect item request is pending')
                        return redirect(request.META['HTTP_REFERER'])
                    except:
                        try:
                            Report.objects.get(allocation=ids, report_action='Return_store')
                            messages.error(request, 'Please Wait Your Return to Store this item request is pending')
                            return redirect(request.META['HTTP_REFERER'])
                        except:
                            Report.objects.get(allocation=ids, report_action='Transfer')
                            messages.error(request, 'Please Wait Your Transfering this item request is pending')
                            return redirect(request.META['HTTP_REFERER'])
        return render(request, "user/service.html")
    else:
        return render(request, "user/service.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

