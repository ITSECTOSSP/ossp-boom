from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def superadmin_dashboard(request):
    return render(request, 'superadmin_dashboard.html')

def superadmin_view_details(request):
    return render(request, 'superadmin_view_details.html')

def employee_dashboard(request):
    return render(request, 'employee_dashboard.html')

def admin_view_details(request):
    return render(request, 'admin_view_details.html')

def admin_dtr(request):
    return render(request, 'admin_dtr.html')

def superadmin_dtr(request):
    return render(request, 'superadmin_dtr.html')

