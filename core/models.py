from django.db import models

# Create your models here.

# SchoolClass Model - Stores Class 1 to 12
class SchoolClass(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Class {self.number}"


# Subject Model - Subject linked to a Class, like Maths, Science
class Subject(models.Model):
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - Class {self.school_class.number}"

    class Meta:
        unique_together = ['school_class', 'name']


# Book Model - Book PDF of one Subject
class Book(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['subject', 'title']


# Note Model - Note PDF of one Subject
class Note(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['subject', 'title']


# Paper Model - Old Paper + Solution for a Subject
class Paper(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    pdf = models.FileField(upload_to='pdfs/')
    solution_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['subject', 'title', 'year']