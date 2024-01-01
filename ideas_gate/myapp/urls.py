"""
URL configuration for ideas_gate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
  
    path('page/<int:pk>/', views.page_detail, name='page_detail'),

    path('add_job/', views.add_job, name='add_job'),  # إضافة هذا السطر
    path('delete_job/<int:pk>/', views.delete_job, name='delete_job'),
    path('edit_job/<int:job_id>/', views.edit_job, name='edit_job'),



]

