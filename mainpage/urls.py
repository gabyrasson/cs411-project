from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.get_search,name='home'),
    url(r'^showprotoresult/$', views.showprotoresult, name='home')
]
