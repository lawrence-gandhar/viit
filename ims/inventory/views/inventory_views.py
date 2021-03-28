"""view inventory file."""

from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.db import IntegrityError

# use below given imports, in case to use the ifm ldap server
# from ..user_login import check_credentials
# from inventory.models import EmployeeMaster


def home(request):
    return render(request,'login.html')

def login(request):
    """Login function for all user."""
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                if user.is_superuser and user.is_staff:
                    auth.login(request,user)
                    return redirect('admins/home')
                elif user.is_staff:
                    auth.login(request,user)
                    return redirect('superuser/home')
                else:
                    auth.login(request,user)
                    return redirect('user/home')
            else:
                messages.info(request,'Account is deactivated Please contact superuser/Admin')
                return render(request,'login.html')
        else:
            messages.info(request,'Invalid Username or Password')
            return render(request,'login.html')

    else:
        return render(request,'login.html')

# def login(request):
#     """function for login feature using ifm LDAP server"""
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         message = check_credentials(username, password)
#         if message == 'loggedin': # check for server response in terms of user_auth.
#             user = auth.authenticate(username=username, password=password)
#             if user is None:
#                 try:
#                     user_obj = User.objects.create_user(username, 'Null@123', password)
#                     employee = EmployeeMaster.objects.create(user=user_obj)# create employee obj too on user creation.
#                     print(user_obj, employee)
#                     employee.save()
#                     user = auth.authenticate(username=username, password=password)
#                 except IntegrityError:
#                     user = auth.authenticate(username=username, password=password)
#             else:
#                 # check for user group separatly
#                 # if user.groups.filter(name='Admin').exists():
#                 #     auth.login(request, user)
#                 #     return redirect('admins/home')
#                 # elif user.groups.filter(name='Superuser').exists():
#                 #     auth.login(request, user)
#                 #     return redirect('superuser/home')
#                 # else:
#                 #     auth.login(request, user)
#                 #     return redirect('user/home')
#                 if user.groups.exists():
#                     auth.login(request, user)
#                     return redirect('login_option', user.id)
#                 else:
#                     auth.login(request, user)
#                     return redirect('user/home')
#
#         else:
#             messages.info(request, 'Invalid Username or Password')
#             return render(request, 'login.html')
#
#     else:
#         return render(request, 'login.html')
#
#     return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def login_option(request, user_id):
    """Login option feature."""

    user = User.objects.get(id=user_id)
    if user.groups.filter(name='Admin').exists():
        admin = 1
    else:
        admin = 0
    if user.groups.filter(name='Superuser').exists():
        superuser = 1
    else:
        superuser = 0


    # to give login options to user on login page [we have used a, RO_1, RO_2]
    return render(request, 'login_option.html', {'id': user.id,
                                                 'admin': admin,
                                                 'superuser': superuser,
                                                 })