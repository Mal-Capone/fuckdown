"""fukdown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_acdata.import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_acdata.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from datetime import datetime

import django.contrib.auth.views

import acdata.forms
import acdata.views
import membership.views

from django.conf.urls import url
from django.conf.urls import include
from django.urls import path
from django.contrib import admin

admin.autodiscover()

acdata.name = 'jazzmin'

urlpatterns = [

    url(r'^$', acdata.views.home, name='home'),
    path('home', acdata.views.home, name="home"),
    path('about', acdata.views.about, name="about"),
    path('users', acdata.views.users, name="users"),
    path('content', acdata.views.content, name="content"),
    path('lists', acdata.views.lists, name="lists"),
    path('services', acdata.views.services, name="services"),

    path('admin/', admin.site.urls),
    path('memberships/', membership.views.MembershipView.as_view(), name='select')
]