from django.db import models

# University Model - GTU, HNGU
class University(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Course Model - Course of one University, like BE IT
class Course(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.university.name})"

    class Meta:
        unique_together = ['university', 'name']


# College Subject Model - Subject of one Course, like Maths
class CollegeSubject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.course.name}"

    class Meta:
        unique_together = ['course', 'name']


# College Book Model - Book PDF of one College Subject
class CollegeBook(models.Model):
    subject = models.ForeignKey(CollegeSubject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['subject', 'title']


# College Note Model - Note PDF of one College Subject
class CollegeNote(models.Model):
    subject = models.ForeignKey(CollegeSubject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['subject', 'title']


# College Paper Model - Old Paper + Solution of one College Subject
class CollegePaper(models.Model):
    subject = models.ForeignKey(CollegeSubject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    pdf = models.FileField(upload_to='pdfs/')
    solution_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['subject', 'title', 'year']