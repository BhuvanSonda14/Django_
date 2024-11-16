from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from django.http import HttpResponse ,JsonResponse,HttpResponseRedirect
from django.template import loader
from .models import *
import json
from django.urls import reverse

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


def Get_Method(request):
    if request.method == 'GET':
        # Fetching all Employee objects from the database (you can adjust this as per your requirements)
        employees = Employee.objects.all()
        response_data = []
        for employee in employees:
            response_data.append({
                'id': employee.id,
                'name': employee.name,
                'email': employee.email,
                'age': employee.age,
                'test': employee.test,
            })
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
  
def delete_employ(request,id):
  employ = Employee.objects.get(id=id)
  template = loader.get_template('delete.html')
  context = {
      'employ':employ
  }
  return HttpResponse(template.render(context, request))
  
def delete(request, id):
  if request.method == 'DELETE':
      item = get_object_or_404(Employee, id=id)
      item.delete()
      return JsonResponse({'message': 'Item deleted successfully!'}, status=200)
  else:
      return JsonResponse({'message': 'Invalid method'}, status=405)


def update(request, id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        employee = get_object_or_404(Employee, id=id)
        employee.name = data.get('name', employee.name)  # Update the name if provided
        employee.save()
        return JsonResponse({'message': 'Employee updated successfully!'}, status=200)
    return JsonResponse({'error': 'Invalid method. Use PUT.'}, status=405)

def update_employ(request,id):
  employ = Employee.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
      'employ':employ
  }
  return HttpResponse(template.render(context, request))
  
def create_employee(request):
    if request.method == "POST":
        try:
            # Load the data from the POST request body
            data = json.loads(request.body)
            
            # Create a new employee object with the provided data
            employee = Employee.objects.create(
                name=data.get("name"),
                email=data.get("email"),
                age=data.get("age"),
                salary=data.get("salary")  
            )

            # Return the newly created employee as a JSON response
            return JsonResponse({
                "id": employee.id,
                "name": employee.name,
                "email": employee.email,
                "age": employee.age,
                "salary": employee.salary,
                "redirect_url": "/Docketrun/get_all_person/"
            }, status=201)
            # return HttpResponseRedirect(reverse('get_all_person'))
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)
 

def insert_employ(request):

  template = loader.get_template('post.html')
  
  return HttpResponse(template.render())