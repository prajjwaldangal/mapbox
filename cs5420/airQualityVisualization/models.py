from django.db import models

# Create your models here.
class SliderData(models.Model):
    date = models.DateTimeField('pick a date')

class PlaceInfo(models.Model):
    aqi = models.CharField(max_length=200)
	
