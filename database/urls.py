from django.conf.urls import url

from database import views

app_name = 'database'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^user/entry/$',views.UserEntry.as_view(),name='user-entry'),

    url(r'^user/(?P<pk>[0-9]+)/$', views.UserUpdate.as_view(), name='user-update'),

    url(r'^album/(?P<pk>[0-9]+)/delete$', views.UserDelete.as_view(), name='user-delete')

]
