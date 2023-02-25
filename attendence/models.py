from django.db import models


# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    fees = models.FloatField()
    credit_hours = models.IntegerField()
    students = models.ManyToManyField('authentication.User', related_name="users")

    def __str__(self):
        return self.name


class Attendance(models.Model):
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()


class Exam(models.Model):
    class ExamType(models.TextChoices):
        MCQ = 'MCQ', 'MCQ'
        TRUEorFalse = 'T-f', 'True or False'
        BOTH = 'BOTH', 'Both'

    # Type: MCQ, T-f, Both
    type = models.CharField(
        max_length=4,
        choices=ExamType.choices,
        default=ExamType.MCQ,
    )
    time = models.DateTimeField()
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="exam", null=True)
    file = models.FileField(null=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Slider(models.Model):
    image = models.ImageField(upload_to='slider')


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    file = models.FileField(null=True)

    def __str__(self):
        return self.title
