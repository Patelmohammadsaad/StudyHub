from rest_framework import serializers
from .models import University, Course, CollegeBook, CollegePaper


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'university']


class CollegeBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeBook
        fields = ['id', 'title', 'course', 'pdf']


class CollegePaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegePaper
        fields = ['id', 'title', 'year', 'course', 'pdf', 'solution_pdf']