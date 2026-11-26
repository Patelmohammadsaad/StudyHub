# Serializer - Convert School data to JSON for App
from rest_framework import serializers
from .models import SchoolClass, Subject, Document, Chapter, Paper


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
        fields = ['id', 'subject', 'title', 'doc_type', 'year', 'chapter', 'solution_pdf', 'pdf']


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'subject', 'number', 'name']


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ['id', 'subject', 'title', 'year', 'pdf', 'solution_pdf']