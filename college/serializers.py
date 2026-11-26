# Serializer - Convert College data to JSON for App
from rest_framework import serializers
from .models import University, Course, Semester, CollegeSubject, CollegeDocument, CollegeChapter, CollegePaper


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'university', 'name']


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ['id', 'course', 'number']


class CollegeSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeSubject
        fields = ['id', 'semester', 'name']


class CollegeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeDocument
        fields = ['id', 'subject', 'title', 'chapter', 'doc_type', 'year', 'pdf']


class CollegeChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeChapter
        fields = ['id', 'subject', 'number', 'name']


class CollegePaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegePaper
        fields = ['id', 'subject', 'title', 'year', 'pdf', 'solution_pdf']