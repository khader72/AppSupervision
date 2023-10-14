from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("host", views.host, name="host"),
    path("hostdel", views.hostdel, name="hostdel"),

    path("service", views.service, name="service"),
    path("servicedel", views.servicedel, name="servicedel"),

    path("equipement", views.equipement, name="equipement"),
    path("equipementdel", views.equipementdel, name="equipementdel"),
    
]