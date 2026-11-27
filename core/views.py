from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SchoolClass, Subject, Book, Note, Paper
from .serializers import SchoolClassSerializer, SubjectSerializer, BookSerializer, NoteSerializer, PaperSerializer

# Home View
def home(request):
    classes = SchoolClass.objects.all().order_by('number')
    from college.models import University
    universities = University.objects.all()
    return render(request, 'core/home.html', {'classes': classes, 'universities': universities})

# School Page View
def school_page(request):
    classes = SchoolClass.objects.all().order_by('number')
    return render(request, 'core/school.html', {'classes': classes})


# Class Detail View - Show Subjects of one Class
def class_detail(request, pk):
    school_class = get_object_or_404(SchoolClass, pk=pk)
    subjects = Subject.objects.filter(school_class=school_class)
    return render(request, 'core/class_detail.html', {'school_class': school_class, 'subjects': subjects})


# Subject Books View - Direct Book PDF open
def subject_books(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    book = Book.objects.filter(subject=subject).first()
    if book:
        return redirect(book.pdf.url)
    return render(request, 'core/subject_books.html', {'subject': subject, 'books': []})


# Subject Notes View - Show Notes list of one Subject
def subject_notes(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    notes = Note.objects.filter(subject=subject)
    return render(request, 'core/subject_notes.html', {'subject': subject, 'notes': notes})

# Subject Papers View - Show Papers of one Subject
def subject_papers(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    papers = Paper.objects.filter(subject=subject).order_by('-year')
    return render(request, 'core/subject_papers.html', {'subject': subject, 'papers': papers})


# //////////////////////////////////////////////////////////////////////////////
# API Views - App ke liye, alag rakha hai


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
def api_papers(request, pk):
    papers = Paper.objects.filter(subject_id=pk).order_by('-year')
    serializer = PaperSerializer(papers, many=True)
    return Response(serializer.data)

