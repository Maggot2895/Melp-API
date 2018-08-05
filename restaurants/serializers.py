from rest_framework import serializers
from .models import Restaurants

class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ('id','rating','name','site','email','phone','street','city','state','lat','lng')