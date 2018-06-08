from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Weather(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    classification = models.CharField(max_length=200)
    temperature = models.IntegerField(default=0)