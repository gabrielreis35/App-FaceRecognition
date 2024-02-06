from django.urls import path
from . import views

urlpatterns = [
    path('', views.listFarmaceuticos, name='listFarmaceuticos'),
    path('create/', views.createFarmaceutico, name='createFarmaceutico'),
    path('update/<int:id>/', views.updateFarmaceutico, name='updateFarmaceutico'),
    path('delete/<int:id>/', views.deleteFarmaceutico, name='deleteFarmaceutico'),
]
