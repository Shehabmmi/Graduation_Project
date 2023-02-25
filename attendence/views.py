from django.http import JsonResponse
from django.shortcuts import render

from attendence.models import Exam


# Create your views here.


def exams(request):
    all_exams = Exam.objects.values('id', 'name', 'type', 'time')
    return JsonResponse({'message': 'success', 'data': list(all_exams)})

