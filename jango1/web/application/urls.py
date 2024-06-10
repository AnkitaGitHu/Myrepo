

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('patient/',views.patient,name="patient"),
    path('services/',views.services,name="services"),
    path('donor/',views.donor,name="donor"),
    path('admin/',views.admin,name="admin"),
]
