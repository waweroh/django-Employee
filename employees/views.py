from django.shortcuts import render, get_object_or_404
from employees.models import Employees
from django.http import Http404, HttpResponse


# Create your views here.

def employee_detail(request, pk):
  # try:
  #   employee = Employees.objects.get(pk=pk)
  #   print(employee)
  # except:
  #   raise Http404
  employee = get_object_or_404(Employees, pk=pk)
  context = {
    'employee': employee
  }
  return render(request,'employee_detail.html',context)