from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('superadmin_view_details/', views.superadmin_view_details, name='superadmin_view_details'),
    path('admin_view_details/', views.admin_view_details, name='admin_view_details'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('admin_dtr/', views.admin_dtr, name='admin_dtr'),
    path('superadmin_dtr/', views.superadmin_dtr, name='superadmin_dtr'),
]