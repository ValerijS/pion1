from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=128, unique=True)
    paycheck = models.IntegerField(default=0)
    date_joined = models.DateField() 
    

    def __unicode__(self):
        return self.name

class Rooms(models.Model):
    depatment = models.CharField(max_length=128)
    spots = models.IntegerField(default=0)

    def __unicode__(self):
        return self.depatment
