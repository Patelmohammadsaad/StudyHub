from django.contrib import admin
from .models import SchoolClass, Subject, Paper, Book, Note

# Register your models here.


admin.site.register(SchoolClass)
admin.site.register(Subject)
admin.site.register(Paper)
admin.site.register(Book)
admin.site.register(Note)