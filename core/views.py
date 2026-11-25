from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import SchoolClass,Subject,Document
from college.models import University


#api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SchoolClassSerializer
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
    subjects = Subject.objects.filter(school_class=school_class)
    return render(request, 'core/class_detail.html', {'school_class': school_class, 'subjects': subjects})


# Subject Detail View - Show papers and books of one subject
def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    documents = Document.objects.filter(subject=subject)
    return render(request, 'core/subject_detail.html', {'subject': subject, 'documents': documents})



# API View - Send Class list as JSON for App
@api_view(['GET'])
def class_list_api(request):
    classes = SchoolClass.objects.all().order_by('number')
    data = SchoolClassSerializer(classes, many=True).data
    return Response(data)
