from rest_framework import serializers
from .models import Puerta, Vuelo

class PuertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puerta
        fields = [
            "id", 
            "code",
            "terminal",
            "is_available",
            "created_at"
        ]

class VueloSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vuelo
        fields = [
            "id", 
            "gate_id", 
            "flight_number", 
            "detination", 
            "status", 
            "departure_time", 
            "created_at"
        ]