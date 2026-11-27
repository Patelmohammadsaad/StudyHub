from django.contrib import admin
from .models import University, Course, CollegeBook, CollegePaper, CollegeSubject, CollegeNote

admin.site.register(University)
admin.site.register(Course)
admin.site.register(CollegeSubject)
admin.site.register(CollegeBook)
admin.site.register(CollegePaper)
admin.site.register(CollegeNote)