from django.db import models

# Create your models here.
class Space(models.Model):
    id = models.AutoField(primary_key=True)
    space_number = models.IntegerField()
    time_in = models.TextField()
    time_out = models.TextField(blank=True)
    price = models.IntegerField(default=-1)
    paid = models.BooleanField(default=False)


class History(models.Model):
    id = models.AutoField(primary_key=True)
    space_number = models.IntegerField()
    time_in = models.TextField()
    time_out = models.TextField(blank=True)
    price = models.IntegerField(default=-1)
    paid = models.BooleanField(default=False)