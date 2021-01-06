from django.shortcuts import render
from rest_framework import generics
from .models import Job, Place, Jobnames
from .serializers import JobSerializer, PlaceSerializer, JobnamesSerializer
# Create your views here.

class Jobview(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetailView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class PlaceListView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceView(generics.CreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class JobnamesListView(generics.ListAPIView):
	queryset = Jobnames.objects.all()
	serializer_class = JobnamesSerializer


class JobnamesCreateView(generics.CreateAPIView):
	queryset = Jobnames.objects.all()
	serializer_class = JobnamesSerializer