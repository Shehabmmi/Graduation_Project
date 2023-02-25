from django.contrib import admin
from django.contrib.auth import get_user_model
from attendence.models import Course
from django.contrib.auth.admin import UserAdmin

# Register your models here.

User = get_user_model()


class CourseInline(admin.TabularInline):
    model = Course.students.through


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [CourseInline, ]

