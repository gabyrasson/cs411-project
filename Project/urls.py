"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from mainpage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('mainpage/', include('mainpage.urls')),
    path('showreports/', views.showreports, include('mainpage.urls')),
    path('handlereport/', views.handlereport, include('mainpage.urls')),
    path('showjobs/', views.showjobs, include('mainpage.urls')),
    path('handlejob/', views.handlejob, include('mainpage.urls')),
    path('handtraing/', views.handtraing, include('mainpage.urls')),
    path('get_token/', views.get_token, include('mainpage.urls')),
    path('add_tasks/', views.show_tasks, include('mainpage.urls')),
]
