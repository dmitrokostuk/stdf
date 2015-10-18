__author__ = 'dmitro'

from django.shortcuts import render
from django.http import HttpResponse


def teacher(request):
    return render(request,'students/teacher.html',{'teacher': teacher})

#def students_add(request):
 #   return HttpResponse('<h1>Student Add Form</h1>')

#def students_edit(request, sid):
 #   return HttpResponse('<h1>Edit Student %s</h1>' % sid)

#def students_delete(request, sid):
 #   return HttpResponse('<h1>Delete Student %s</h1>' % sid)
