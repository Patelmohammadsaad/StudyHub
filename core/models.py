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
        return f"{self.name} - Class {self.school_class.number}"


# Chapter Model - Chapter of a Subject for Books, Notes and Questions
class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
     return f"Chapter {self.number} - {self.name} ({self.subject.name} - Class {self.subject.school_class.number})"


# Document Model - Old Paper or Book PDF for a Subject
class Document(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    doc_type = models.CharField(max_length=20)
    year = models.IntegerField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True, blank=True)
    solution_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title

# Paper Model - Old Paper + Solution for a Subject
class Paper(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    pdf = models.FileField(upload_to='pdfs/')
    solution_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.title