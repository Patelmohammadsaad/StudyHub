from django.contrib import admin
from .models import University, Course, Semester, CollegeSubject, CollegeDocument,CollegeChapter,CollegePaper

# Register your models here.


admin.site.register(University)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(CollegeSubject)
admin.site.register(CollegeDocument)
admin.site.register(CollegeChapter)
admin.site.register(CollegePaper)
