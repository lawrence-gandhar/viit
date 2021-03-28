"""superuser urls file."""

from django.urls import path

from inventory.views import superuser_views

urlpatterns=[
    path('home',superuser_views.home,name='superuser_home'),
    path('<allo_id>/info',superuser_views.info,name='info'),
    path('<allo_id>/create',superuser_views.create,name='create'),
    path('<allo_id>/accept',superuser_views.accept,name='accept'),
    path('<allo_id>/reject',superuser_views.reject,name='reject'),

    path('<allo_id>/accept1',superuser_views.accept1,name='accept1'),
    path('<allo_id>/reject1',superuser_views.reject1,name='reject1'),

    path('search_items',superuser_views.search_items,name='search_items'),
    path('modify_items',superuser_views.modify_items,name='edit_item'),
    path('<allo_id>/details',superuser_views.details,name='details'),
    path('add',superuser_views.add,name='add_items'),
    path('<allo_id>/delete',superuser_views.delete,name='delete'),
    path('ldap',superuser_views.ldap,name='ldap'),
    path('disallow',superuser_views.disallow,name='disallow'),
    path('allow',superuser_views.allow,name='allow'),
    path('logout',superuser_views.logout,name='logout'),
    path('<allo_id>/delete',superuser_views.delete,name='delete'),
]
