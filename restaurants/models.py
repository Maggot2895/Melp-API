# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Restaurants(models.Model):
    id = models.CharField(primary_key = True, max_length = 255)
    rating = models.IntegerField()
    name = models.CharField(max_length = 255)
    site = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 255)
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 255)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name

