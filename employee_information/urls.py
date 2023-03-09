from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('', views.home, name="home-page"),
    path('login', auth_views.LoginView.as_view(template_name = 'employee_information/login.html',redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logoutuser, name="logout"),
    path('about', views.about, name="about-page"),
    path('department', views.department, name="department-page"),
    path('manage_department', views.manage_department, name="manage_department-page"),
    path('save_department', views.save_department, name="save-department-page"),
    path('delete_department', views.delete_department, name="delete-department"),
    path('position', views.position, name="position-page"),
    path('manage_position', views.manage_position, name="manage_positions-page"),
    path('save_position', views.save_position, name="save-position-page"),
    path('delete_position', views.delete_position, name="delete-position"),
    path('employee', views.employee, name="employee-page"),
    path('manage_employee', views.manage_employee, name="manage_employee-page"),
    path('save_employee', views.save_employee, name="save-employee-page"),
    path('delete_employee', views.delete_employee, name="delete-employee"),
    path('view_employee', views.view_employee, name="view-employee-page"),
]