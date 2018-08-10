# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, views, response, generics
from .models import Restaurants
from .serializers import RestaurantsSerializer
from statistics import stdev
from rest_framework.renderers import JSONRenderer

# Create your views here.

class RestaurantsView(viewsets.ModelViewSet):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer

class StatisticView(views.APIView):

    serializer_class = RestaurantsSerializer
    renderer_classes = (JSONRenderer,)

    def get(self,request):
        queryset = Restaurants.objects.all()
        lat = self.request.query_params.get('latitude',None)
        lon = self.request.query_params.get('longitude',None)
        rad = self.request.query_params.get('radius',None)
        
        #Limit defintion
        xneg = float(lat) - float(rad) 
        xpos = float(lat) + float(rad)
        yneg = float(lon) - float(rad)
        ypos = float(lon) + float(rad)

        contador = 0
        avg = [0]

        for cont in queryset:
            lat_ref = cont.lat
            lon_ref = cont.lng
            if lat_ref > xneg and lat_ref < xpos and lon_ref > yneg and lon_ref < ypos:
                contador = contador + 1
                avg.append(cont.rating)
        
        if contador != 0:
            #Average of the restaurants that fall into the circle
            avgTot = 0.0
            for n in range(len(avg)):
                avgTot = avgTot + avg[n]
            avgTot = avgTot/contador
 
            #Standard deviation of rating of restaurants inside de circle
            standDev = stdev(avg) 

            content = {'count' : contador,'avg' : avgTot,'std' : standDev}

            return response.Response(content)
        
        else:
            content = {'count' : 0,'avg' : 0,'std' : 0}

            return response.Response(content)

          

        
        
        

