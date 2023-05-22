from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class CompanyView(APIView):
    def get(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg':'New data has been created successfully'}
            return Response(msg)
    def delete(self, request):
        cmp = request.data
        id = cmp.get('id')
        cmp = Company.objects.get(id=id)
        cmp.delete()
        msg = {'msg':'The company has been deleted successfully'}
        return Response(msg)


class EmployeeView(APIView):
    def get(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg':'New data has been created successfully'}
            return Response(msg)
    def delete(self, request):
        emp = request.data
        id = emp.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg = {'msg':'The employee has been deleted successfully'}
        return Response(msg)



class DeviceView(APIView):
    def get(self, request):
        queryset = Device.objects.all()
        serializer = DeviceSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        serializer = DeviceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg':'New data has been created successfully'}
            return Response(msg)
    def delete(self, request):
        dev = request.data
        id = dev.get('id')
        dev = Device.objects.get(id=id)
        dev.delete()
        msg = {'msg':'The device has been deleted successfully'}
        return Response(msg)



class AssignmentView(APIView):
    def get(self, request):
        queryset = Device_Assignment.objects.all()
        serializer = AssignmentSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        serializer = AssignmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg':'New data has been created successfully'}
            return Response(msg)
    def delete(self, request):
        dev = request.data
        id = dev.get('id')
        dev = Device_Assignment.objects.get(id=id)
        dev.delete()
        msg = {'msg':'The device assignment has been deleted successfully'}
        return Response(msg)

