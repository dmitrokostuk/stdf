
from django.shortcuts import render
from django.http import HttpResponse
from ..models import Exams
def exams_list(request):
    exams = Exams.objects.all()

    return render(request, 'students/exams_list.html',
        {'exams': exams})

def exams_add(request):
    return HttpResponse('<h1>Exam Add Form</h1>')

def exams_edit(request, gid):
    return HttpResponse('<h1>Edit Exam %s</h1>' % gid)

def exams_delete(request, gid):
    return HttpResponse('<h1>Delete Exam %s</h1>' % gid)