from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    url('^$', views.get_search, name='home'),
    url(r'^showprotoresult/$', views.showprotoresult, name='home'),
    path('showreports/<str:country>/<str:distype>', views.showreports, name="showreports"),
    path('showjobs/<str:country>', views.showjobs, name="showjobs")
]
