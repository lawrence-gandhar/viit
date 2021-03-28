"""user urls file."""

from django.urls import path
from django.conf.urls.static import static
from inventory.views import user_views

urlpatterns=[
    path('home',user_views.home,name='user_home'),
    path('<allo_id>/create_service',user_views.create_service,name='create_service'),
    path('<allo_id>/Information',user_views.Information,name='Information'),
    path('<allo_id>/Return_to_store',user_views.Return_to_store,name='Return_to_store'),
    path('<allo_id>/Free_Item',user_views.Free_Item,name='Free_Item'),
    path('<allo_id>/Transfer',user_views.Transfer,name='Transfer'),
    path('<allo_id>/incorrect',user_views.incorrect,name='incorrect'),
    path('search',user_views.search,name='search'),
    path('<allo_id>/release',user_views.release,name='release'),
    path('<allo_id>/borrow',user_views.borrow,name='borrow'),
    path('<allo_id>/details',user_views.details,name='detail'),
    path('advance',user_views.advance,name='advance'),
    path('<allo_id>/tp',user_views.tp,name='tp'),
    path('service',user_views.service,name='service'),
    path('incorrect1',user_views.incorrect1,name='incorrect1'),
    path('Return_to_store1',user_views.Return_to_store1,name='Return_to_store1'),
    path('Free_Item1',user_views.Free_Item1,name='Free_Item1'),
    path('Project_list',user_views.projectlist,name='Project_list'),
    path('<allo_id>/Proj_info',user_views.project_info,name='Proj_info'),
    path('search_items',user_views.search_items,name='user_search_items'),
]