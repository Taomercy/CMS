"""CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path

from CMS.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', index, name='index'),

    re_path(r'^family_display', family_display, name='family_display'),
    re_path(r'^family_create', family_create, name='family_create'),
    re_path(r'^family_details', family_details, name='family_details'),
    re_path(r'^family_member_create', family_member_create, name='family_member_create'),
    re_path(r'^family_member_invite', family_member_invite, name='family_member_invite'),

    re_path(r'^person_display', person_display, name='person_display'),
    re_path(r'^person_family_display', person_family_display, name='person_family_display'),

    re_path(r'^affair_create', affair_create, name='affair_create'),
    re_path(r'^affairs_display', affairs_display, name='affairs_display'),

    re_path(r'^backup_manually', backup_manually, name='backup_manually'),

    re_path(r'^index2', index2, name='index2'),

    re_path(r'^statistic_to_excel', statistic_to_excel, name='statistic_to_excel'),
    re_path(r'^upload_file', upload_file, name='upload_file'),
    re_path(r'^download_file', download_file, name='download_file'),
    re_path(r'^download_information_template', download_information_template, name='download_information_template'),
]
