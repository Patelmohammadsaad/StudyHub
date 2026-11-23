from django.contrib import admin
from .models import SchoolClass, Subject, Document

# Register your models here.


admin.site.register(SchoolClass)
admin.site.register(Subject)
admin.site.register(Document)
