from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import University, Course, CollegeSubject, CollegeBook, CollegePaper, CollegeNote
from .serializers import UniversitySerializer, CourseSerializer, CollegeBookSerializer, CollegePaperSerializer


# College Home View - Show Universities
def college_home(request):
    universities = University.objects.all()
    return render(request, 'college/college_home.html', {'universities': universities})


# University Detail View - Show Courses of one University
def university_detail(request, pk):
    university = get_object_or_404(University, pk=pk)
    courses = Course.objects.filter(university=university)
    return render(request, 'college/university_detail.html', {'university': university, 'courses': courses})


# Course Detail View - Show Subjects of one Course
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    subjects = CollegeSubject.objects.filter(course=course)
    return render(request, 'college/course_detail.html', {'course': course, 'subjects': subjects})


# College Subject Books View - Direct Book PDF open
def course_books(request, pk):
    subject = get_object_or_404(CollegeSubject, pk=pk)
    book = CollegeBook.objects.filter(subject=subject).first()
    if book:
        return redirect(book.pdf.url)
    return render(request, 'college/course_books.html', {'subject': subject, 'books': []})


# College Subject Papers View - Show Old Papers of one Subject
def course_papers(request, pk):
    subject = get_object_or_404(CollegeSubject, pk=pk)
    papers = CollegePaper.objects.filter(subject=subject).order_by('-year')
    return render(request, 'college/course_papers.html', {'subject': subject, 'papers': papers})

# College Subject Notes View - Show Notes list of one Subject
def course_notes(request, pk):
    subject = get_object_or_404(CollegeSubject, pk=pk)
    notes = CollegeNote.objects.filter(subject=subject)
    return render(request, 'college/course_notes.html', {'subject': subject, 'notes': notes})

# //////////////////////////////////////////////////////////////////////////////
# API Views - App ke liye, alag rakha hai


@api_view(['GET'])
def api_universities(request):
    universities = University.objects.all()
    serializer = UniversitySerializer(universities, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_courses(request, pk):
    courses = Course.objects.filter(university_id=pk)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_books(request, pk):
    books = CollegeBook.objects.filter(course_id=pk)
    serializer = CollegeBookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_papers(request, pk):
    papers = CollegePaper.objects.filter(course_id=pk).order_by('-year')
    serializer = CollegePaperSerializer(papers, many=True)
    return Response(serializer.data)