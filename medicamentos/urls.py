from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.listMedicamentos, name='listMedicamentos'),
    path('create/', views.createMedicamento, name='createMedicamentos'),
]