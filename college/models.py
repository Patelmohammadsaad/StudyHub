from django.db import models

# Create your models here.

# University Model - Stores HNGU, GTU, etc.
class University(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Course Model - Course linked to a University, like B.E. IT, B.Com
class Course(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Semester Model - Semester linked to a Course, like Sem 1, Sem 2
class Semester(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f"Sem {self.number}"



# CollegeSubject Model - Subject linked to a Course, like Maths, Python
class CollegeSubject(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# CollegeDocument Model - Old Paper or Solution PDF for a College Subject
class CollegeDocument(models.Model):
    subject = models.ForeignKey(CollegeSubject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    doc_type = models.CharField(max_length=20)
    year = models.IntegerField()
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title
