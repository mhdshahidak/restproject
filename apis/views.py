from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from . models import student
from .serializers import StudentSerializer
# Create your views here.

class Student(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        serializer.save(age = '22')