from django.db import models

# Create your models here.

# SchoolClass Model - Stores Class 1 to 12
class SchoolClass(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Class {self.number}"


# Subject Model - Subject linked to a Class, like Maths, Science
class Subject(models.Model):
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Document Model - Old Paper or Book PDF for a Subject
class Document(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    doc_type = models.CharField(max_length=20)
    year = models.IntegerField()
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title
