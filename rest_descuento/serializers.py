from dataclasses import fields
from rest_framework import serializers
from CommunityPlant.models import Descuento

class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descuento
        fields = ['IdCodigo','Porcentaje']