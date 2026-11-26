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
        return f"{self.name} ({self.university.name})"


# Semester Model - Semester linked to a Course, like Sem 1, Sem 2
class Semester(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f"Sem {self.number} - {self.course.name} ({self.course.university.name})"


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
    chapter = models.ForeignKey('CollegeChapter', on_delete=models.CASCADE, null=True, blank=True)
    doc_type = models.CharField(max_length=20)
    year = models.IntegerField()
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title



# College Chapter Model - Chapter for a College Subject
class CollegeChapter(models.Model):
    subject = models.ForeignKey(CollegeSubject, on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Chapter {self.number} - {self.name} ({self.subject.name})"


# College Paper Model - Old Paper + Solution for a College Subject
class CollegePaper(models.Model):
    subject = models.ForeignKey(CollegeSubject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    pdf = models.FileField(upload_to='pdfs/')
    solution_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.title