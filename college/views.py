from django.shortcuts import render
from .models import University, Course, Semester, CollegeSubject, CollegeDocument, CollegeChapter, CollegePaper

from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UniversitySerializer, CourseSerializer, SemesterSerializer, CollegeSubjectSerializer, CollegeDocumentSerializer

# Create your views here.

# College Home View - Show Universities like GTU, HNGU
def college_home(request):
    universities = University.objects.all()
    return render(request, 'college/college_home.html', {'universities': universities})



# University Detail View - Show courses of one university
def university_detail(request, pk):
    university = get_object_or_404(University, pk=pk)
    courses = Course.objects.filter(university=university)
    return render(request, 'college/university_detail.html', {'university': university, 'courses': courses})



# Course Detail View - Show semesters of one course
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    semesters = Semester.objects.filter(course=course).order_by('number')
    return render(request, 'college/course_detail.html', {'course': course, 'semesters': semesters})



# Semester Detail View - Show subjects of one semester
def semester_detail(request, pk):
    semester = get_object_or_404(Semester, pk=pk)
    subjects = CollegeSubject.objects.filter(semester=semester)
    return render(request, 'college/semester_detail.html', {'semester': semester, 'subjects': subjects})



# # College Subject Detail View - Show papers and solutions of one subject
# def college_subject_detail(request, pk):
#     subject = get_object_or_404(CollegeSubject, pk=pk)
#     documents = CollegeDocument.objects.filter(subject=subject)
#     return render(request, 'college/college_subject_detail.html', {'subject': subject, 'documents': documents})



# College Subject Chapters View - Show only Chapters of one College Subject
def college_subject_chapters(request, pk):
    subject = get_object_or_404(CollegeSubject, pk=pk)
    chapters = CollegeChapter.objects.filter(subject=subject).order_by('number')
    return render(request, 'college/college_subject_chapters.html', {'subject': subject, 'chapters': chapters})


# College Subject Papers View - Show only Papers of one College Subject
def college_subject_papers(request, pk):
    subject = get_object_or_404(CollegeSubject, pk=pk)
    papers = CollegePaper.objects.filter(subject=subject).order_by('-year')
    return render(request, 'college/college_subject_papers.html', {'subject': subject, 'papers': papers})


# College Chapter Detail View - Show Books and Questions of one Chapter
def college_chapter_detail(request, pk):
    chapter = get_object_or_404(CollegeChapter, pk=pk)
    documents = CollegeDocument.objects.filter(chapter=chapter).order_by('doc_type', 'title')
    return render(request, 'college/college_chapter_detail.html', {'chapter': chapter, 'documents': documents})

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# API Views - App ke liye JSON data
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
def api_semesters(request, pk):
    semesters = Semester.objects.filter(course_id=pk).order_by('number')
    serializer = SemesterSerializer(semesters, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_college_subjects(request, pk):
    subjects = CollegeSubject.objects.filter(semester_id=pk)
    serializer = CollegeSubjectSerializer(subjects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_college_documents(request, pk):
    documents = CollegeDocument.objects.filter(subject_id=pk)
    serializer = CollegeDocumentSerializer(documents, many=True)
    return Response(serializer.data)