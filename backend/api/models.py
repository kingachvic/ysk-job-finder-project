from django.db import models

# Create your models here.
class Place(models.Model):
    county = models.CharField(max_length=200)
    subcounty = models.CharField(max_length=200)
    ward = models.CharField(max_length=200)

    def __str__(self):
        return self.ward

class Job(models.Model):

    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    
    kinyozi = models.CharField(max_length=200, default='kinyozi')
    chips = models.CharField(max_length=200, default='chips')
    kiosk = models.CharField(max_length=200, default='kiosk')
    water = models.CharField(max_length=200, default='water')
    art = models.CharField(max_length=200, default='art')
    carwash = models.CharField(max_length=200, default='carwash')
    cyber = models.CharField(max_length=200, default='cyber')
    mkokoteni = models.CharField(max_length=200, default='mkokoteni')
    tea = models.CharField(max_length=200, default='tea')
    cobler = models.CharField(max_length=200, default='cobler')
    mutura = models.CharField(max_length=200, default='mutura')
    eggs = models.CharField(max_length=200, default='eggs')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return ('jobs in '+self.place.ward)

class Jobnames(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    kinyozi = models.IntegerField(default=0)
    chips = models.IntegerField(default=0)
    kiosk = models.IntegerField(default=0)
    water = models.IntegerField(default=0)
    art = models.IntegerField(default=0)
    carwash = models.IntegerField(default=0)
    cyber = models.IntegerField(default=0)
    mkokoteni = models.IntegerField(default=0)
    tea = models.IntegerField(default=0)
    cobler = models.IntegerField(default=0)
    mutura = models.IntegerField(default=0)
    eggs = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return ('jobs in '+self.place.ward)