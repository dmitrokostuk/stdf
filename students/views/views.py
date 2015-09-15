# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

# Create your views here.

def students_list(request):
    students = (
        {'id': 1,
         'first_name' : u'Дмитро',
         'last_name': u'Костюк',
         'ticket' : 1222,
         'image':'img/kosmos.jpg'
         },
        {'id':2,
         'first_name' : u'Василів',
         'last_name': u'Василь',
         'ticket' : 12,
         'image':'img/kosmos.jpg'},
        {'id':3,
         'first_name' : u'Петрів',
         'last_name': u'Петро',
         'ticket' : 12123,
         'image':'img/kosmos.jpg'},
     )
    return render(request,'students/students_list.html',{'students':students})


def students_add(request):

    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

#Viev for Groups

def groups_list(request):
    return render(request,'students/groups.html')

    #return HttpResponse('<h1>Groups Listing </h1>')

def groups_add(request):
    return HttpResponse('<h1>Groups Add Form </h1>')

def groups_edit(request,gid):
    return HttpResponse('<h1>Edit Group %s  </h1>' % gid)

def groups_delete(request,gid):
    return HttpResponse('<h1> Delete Group %s </h1>'% gid)

