# Serializer - Convert SchoolClass data to JSON for App
from rest_framework import serializers
from .models import SchoolClass, Subject, Document


class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ['id', 'number', 'name']
 
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'school_class', 'name']


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'subject', 'title', 'doc_type', 'year', 'pdf']