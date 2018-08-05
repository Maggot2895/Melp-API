# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import Restaurants
from .serializers import RestaurantsSerializer

# Create your views here.

class RestaurantsView(viewsets.ModelViewSet):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer
    
