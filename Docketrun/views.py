from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from django.template import loader
from .models import *

def response(request):
    template=loader.get_template("docketrun.html")
    return HttpResponse(template.render())

def get_all_person(request):
    latest_employ=Employee.objects.order_by("id")
    template = loader.get_template("get_all_person.html")
    context = {
        "latest_employ": latest_employ,
    }
    return HttpResponse(template.render(context, request))

def All_employs(request):
    latest_employ=Employee.objects.order_by("id")
    template = loader.get_template("All_employs.html")
    context = {
        "latest_employ": latest_employ,
    }
    return HttpResponse(template.render(context, request))

def employ_details(request,id):
  employ = Employee.objects.get(id=id)
  template = loader.get_template('employ_details.html')
  context = {
      'employ':employ
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def testing(request):
  mydata = Employee.objects.all()
  template = loader.get_template('table.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request)) 

def filter(request):
  # print("HTTP Method:", request.method)                # GET or POST
  # print("Query Parameters:", request.GET)              # Query parameters in a GET request
  # print("Form Data:", request.POST)                    # Form data in a POST request
  # print("Cookies:", request.COOKIES)                   # Cookies sent by the client
  # print("Session Data:", request.session.get('user'))  # Session data for the user
  # print("User:", request.user)                         # Authenticated user, if any
  # print("Headers:", request.headers)                   # HTTP headers
  print("Path:", request.path) 
  # print("This is he Http request  ",request)
  mydata = Employee.objects.filter(name="name")
  template = loader.get_template('filter.html')
  context = {
    'mymember': mydata,
  }
  return HttpResponse(template.render(context, request))


def filter_person(request):
    # Get the name parameter from the GET request (if it exists)
    name_filter = request.GET.get('name', '')

    # If a name was provided, filter the employees by that name (case-sensitive)
    if name_filter:
        mydata = Employee.objects.filter(name__contains=name_filter)  
    else:
        mydata = "" 
    return render(request, 'filter_person.html', {'mymember': mydata, "all": Employee.objects.all()})

def slug_view(request,slug):
    latest_employ=Final_trial.objects.filter(slug=slug)
    template = loader.get_template("filter.html")
    context = {
        "mymembers": latest_employ}
    return HttpResponse(template.render(context, request))