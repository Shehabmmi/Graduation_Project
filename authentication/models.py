from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

from attendence.models import Course
# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    # courses = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    class UserType(models.TextChoices):
        STUDENT = 'ST', 'Student'
        DOCTOR = 'DR', 'Doctor'
        ADMIN = 'AD', 'Admin'

    type = models.CharField(
        max_length=2,
        choices=UserType.choices,
        default=UserType.STUDENT,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     # TODO Make the courses a relation
#     courses = models.CharField(max_length=255)
#
#
# class Doctor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     # TODO Make the courses a relation
#     courses = models.CharField(max_length=255)
