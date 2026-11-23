from django.shortcuts import render
from .models import University,Course,Semester,CollegeSubject,CollegeDocument

from django.shortcuts import get_object_or_404

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



# College Subject Detail View - Show papers and solutions of one subject
def college_subject_detail(request, pk):
    subject = get_object_or_404(CollegeSubject, pk=pk)
    documents = CollegeDocument.objects.filter(subject=subject)
    return render(request, 'college/college_subject_detail.html', {'subject': subject, 'documents': documents})
