from django.contrib import admin
from .models import SchoolClass, Subject, Document,Chapter,Paper

# Register your models here.


admin.site.register(SchoolClass)
admin.site.register(Subject)
admin.site.register(Document)
admin.site.register(Chapter)
admin.site.register(Paper)