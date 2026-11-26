from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import SchoolClass, Subject, Chapter, Document
from college.models import University


# api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SchoolClassSerializer, SubjectSerializer, DocumentSerializer
# Create your views here.


# Home View - Show Class 1 to 12
def home(request):
    classes = SchoolClass.objects.all()
    universities = University.objects.all()
    return render(request, 'core/home.html', {'classes': classes, 'universities': universities})


def school_page(request):
    classes = SchoolClass.objects.all()
    return render(request, 'core/school.html', {'classes': classes})


# Class Detail View - Show subjects of one class
def class_detail(request, pk):
    school_class = get_object_or_404(SchoolClass, pk=pk)
    subjects = Subject.objects.filter(school_class=school_class).order_by('name')
    return render(request, 'core/class_detail.html', {'school_class': school_class, 'subjects': subjects})


# Chapter Detail View - Show Books, Notes and Questions of one Chapter
def chapter_detail(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    documents = Document.objects.filter(chapter=chapter).order_by('doc_type', 'title')
    return render(request, 'core/chapter_detail.html', {'chapter': chapter, 'documents': documents})


# # Subject Detail View - Show Chapters and Papers of one Subject
# def subject_detail(request, pk):
#     subject = get_object_or_404(Subject, pk=pk)
#     chapters = Chapter.objects.filter(subject=subject).order_by('number')
#     papers = Document.objects.filter(subject=subject, chapter__isnull=True).order_by('-year')
#     return render(request, 'core/subject_detail.html', {'subject': subject, 'chapters': chapters, 'papers': papers})


# Subject Chapters View - Show only Chapters of one Subject
def subject_chapters(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    chapters = Chapter.objects.filter(subject=subject).order_by('number')
    return render(request, 'core/subject_chapters.html', {'subject': subject, 'chapters': chapters})


# Subject Papers View - Show only Papers of one Subject
def subject_papers(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    papers = Document.objects.filter(subject=subject, chapter__isnull=True).order_by('-year')
    return render(request, 'core/subject_papers.html', {'subject': subject, 'papers': papers})







# API View - Send Class list as JSON for App
@api_view(['GET'])
def class_list_api(request):
    classes = SchoolClass.objects.all().order_by('number')
    data = SchoolClassSerializer(classes, many=True).data
    return Response(data)



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# API Views - App ke liye JSON data
@api_view(['GET'])
def api_classes(request):
    classes = SchoolClass.objects.all().order_by('number')
    serializer = SchoolClassSerializer(classes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_subjects(request, pk):
    subjects = Subject.objects.filter(school_class_id=pk)
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_documents(request, pk):
    documents = Document.objects.filter(subject_id=pk)
    serializer = DocumentSerializer(documents, many=True)
    return Response(serializer.data)