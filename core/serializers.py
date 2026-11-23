# Serializer - Convert SchoolClass data to JSON for App
from rest_framework import serializers
from .models import SchoolClass

class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ['id', 'number', 'name']
