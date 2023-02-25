from django.contrib import admin
from .models import Course, Attendance, Exam, Slider, Announcement, Session

# Register your models here.


admin.site.register(Course)
admin.site.register(Attendance)
admin.site.register(Exam)
admin.site.register(Slider)
admin.site.register(Announcement)
admin.site.register(Session)
