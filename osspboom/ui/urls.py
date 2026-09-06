from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('superadmin_view_details/', views.superadmin_view_details, name='superadmin_view_details'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
]