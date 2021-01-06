from rest_framework import serializers
from .models import Job, Place, Jobnames

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('__all__')
        
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('__all__')

class JobnamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobnames
        fields = ('__all__')