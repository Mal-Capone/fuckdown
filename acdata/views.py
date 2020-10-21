""" Definition of views"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext

sep = " | "
version = 1
company_name = 'AC Data Managment'

def base(request):
    assert isinstance(request, HttpRequest)
    ctx = {
        'company' : 'AC Data Management',
        'version' : '1.00',
        'title'   : '',
        'heading' : None,
        'year'    : datetime.now().year}
    return ctx

def about(request):
    assert isinstance(request, HttpRequest)
    ctx = {
        'title'   : 'About Us',
        'heading' : 'About AC-Admin',
        'company' : 'AC Data Management',
        'year': datetime.now().year}
    return render(request, 'acdata/about.html', context=ctx)

def content(request):
    assert isinstance(request, HttpRequest)
    ctx = {
        'company' : 'AC Data Management',
        'title'   : 'Content Management | AC Data Services',
        'heading' : 'Manage Website Content',
        'year'    :  datetime.now().year
    }
    return render(request, 'acdata/content.html', context=ctx)

def home(request):
    """Renders the home page."""
    ctx = base(request)
    ctx['title']   ='Home Page'
    ctx['heading'] ='Dashboard Homescreen'
    return render(request, 'acdata/home.html', context=ctx)

def lists(request):
    assert isinstance(request, HttpRequest)
    ctx = {
        'company' : 'AC Data Management',
        'title'   : 'B2B Lists | AC Data Management',
        'heading' : 'B2B List Builder',
        'year'    :  datetime.now().year
    }
    return render(request, 'acdata/lists.html', context=ctx)

def services(request):
    assert isinstance(request, HttpRequest)
    ctx = {
        'title'   : f'Services | {company_name}',
        'heading' : f'My Services',
        'company' : company_name,
        'year'    : datetime.now().year}
    return render(request, 'acdata/services.html', context=ctx)

def settings(request):
    assert isinstance(request, HttpRequest)
    ctx = {
        'title'   : f'Services | {company_name}',
        'heading' : f'My Services',
        'company' : company_name,
        'year'    : datetime.now().year}
    return render(request, 'acdata/services.html', context=ctx)

def users(request):
    assert isinstance(request, HttpRequest)
    ctx = {
        'title'   : f'Manage Users | {company_name}',
        'heading' : 'User Management',
        'company' :  company_name,
        'year'    :  datetime.now().year}
    return render(request, 'acdata/users.html', context=ctx)

