# Courses/views.py
from django.shortcuts import render, get_list_or_404
from .models import Courses

def course_list(request):
    courses = Courses.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_list_or_404(Courses, pk=pk)
    return render(request, 'course_detail.html', {'course': course})
