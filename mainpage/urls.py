from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    url('^$', views.get_search, name='home'),
    url(r'^showprotoresult/$', views.showprotoresult, name='home'),
    path('showreports/<str:country>/<str:distype>/', views.showreports, name="showreports"),
    path('handlereport/<str:reportid>/', views.handlereport, name="handlereport"),
    path('showjobs/<str:country>/', views.showjobs, name="showjobs"),
    path('handlejob/<str:jobid>/', views.handlejob, name="handlejob"),
    path('handtraing/<str:traingid>/', views.handtraing, name="handtraing"),
    path('get_token/', views.get_token, name="get_token"),
    path('add_tasks/<str:title>/<str: duedate>', views.show_tasks, name="show_tasks"),
]
