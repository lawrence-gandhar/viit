"""admin urls file. """

from django.urls import path

from inventory.views import admin_views

urlpatterns=[
    path('home',admin_views.home,name='admin_home'),
    path('logout',admin_views.logout,name='logout'),
    path('ldaps',admin_views.ldaps,name='ldaps'),
    path('disallow',admin_views.disallow,name='disallow'),
    path('allow',admin_views.allow,name='allow'),
    path('add',admin_views.add,name='add'),
    path('edit',admin_views.modify_item,name='modify_items'),
    path('search_items',admin_views.search_items,name='admin_search_items'),
]
