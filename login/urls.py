from django.urls import re_path as url
from .views import (LoginView,
                    LogOutView,
                    UserListViewAll,
                    UserCreateView,
                    UserProfileCreateView
               )

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogOutView.as_view(), name='logout'),
    url(r'^listar/$', UserListViewAll.as_view(), name='listar'),
    url(r'^cadastro/$', UserCreateView.as_view(), name='cadastro'),
    url(r'^userProfile/$', UserProfileCreateView.as_view(), name='cadastro'),

]