from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import viewsets, generics 
from post.serializers import *
from post.models import *

# Create your views here. it s display data..
# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello world!")

from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
from .models import employee
from .serializers import employeeSerializer



# advance level code ..... for Get Data
class employeeList (generics.ListCreateAPIView):
    serializer_class = employeeSerializer
    queryset = employee.objects.all()


class employeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

# @csrf_exempt
# def employeeList(request,id=0):
#     if request.method=='GET':
#         employees = employee.objects.all()
#         employees_serializer=employeeSerializer(employees,many=True)
#         return JsonResponse(employees_serializer.data,safe=False)
#     elif request.method=='POST':
#         employee_data=JSONParser().parse(request)
#         employees_serializer=employeeSerializer(data=employee_data)
#         if employees_serializer.is_valid():
#             employees_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)

#     # elif request.method=='PUT':
#     #     employee_data=JSONParser().parse(request)
#     #     employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
#     #     employees_serializer=employeeSerializer(employee,data=employee_data)
#     #     if employees_serializer.is_valid():
#     #         employees_serializer.save()
#     #         return JsonResponse("Updated Successfully",safe=False)
#     #     return JsonResponse("Failed to Update")
#     # elif request.method=='DELETE':
#     #     employee=Employees.objects.get(EmployeeId=id)
#     #     employee.delete()
#     #     return JsonResponse("Deleted Successfully",safe=False)
 



