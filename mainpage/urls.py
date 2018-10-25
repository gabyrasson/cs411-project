from django.urls import path
from . import views
urlpatterns = [
    path('', views.showprotoresult, name = 'showprotoresult'),
]