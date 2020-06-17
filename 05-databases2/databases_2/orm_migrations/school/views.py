from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    students_list = Student.objects.all().prefetch_related('teacher').order_by(ordering)

    context = {
        'object_list': students_list
    }
    return render(request, template, context)
