# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from ..models import Student, Group

def students_list(request):
    students = Student.objects.all()
    #try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name','first_name','ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse','') == '1':
            students = students.reverse()
    #paginate students
    paginator = Paginator(students,4)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer,deliver first page
        students = paginator.page(1)
    except EmptyPage:
        #If page is out of range (e.g. 9999),deliver
        #lasp page od results
        students = paginator.page(paginator.num_pages)

    return render(request,'students/students_list.html',{'students': students})

def students_add(request):
    # was posted form&
    if request.method == "POST":
        #was form add button clicked&
        if request.POST.get('add_button') is not None:
            # TODO: validate input from user
            errors = {}
            #validate student data will go here
            data = {'middle_name':request.POST.get('middle_name'),
                    'notes':request.POST.get('notes')}
            #validate user input
            first_name = request.POST.get('first_name','').strip()
            if not first_name:
                errors['first_name'] = u"Імя є обовязковим"
            else:
                data['first-name'] = first_name

            last_name = request.POST.get('last_name','').strip()
            if not last_name:
                errors['last_name'] = u"Прізвище є обовязковим "
            else:
                data['lasts_name'] = last_name

            birthday = request.POST.get('birthday','').strip()
            if not birthday:
                errors['birthday'] = u"Прізвище є обовязковим "
            else:
                data['birthday'] = birthday

            ticket = request.POST.get('ticket','').strip()
            if not last_name:
                errors['ticket'] = u"Прізвище є обовязковим "
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group','').strip()
            if not last_name:
                errors['student_group'] = u"Прізвище є обовязковим "
            else:
                data['student_group'] = Group.objects.get(pk=student_group)

            photo = request.FILES.get('photo')
            if photo:
                data['photo']





        if not errors:
            #create student object
           student = Student(**data)
           # save it to database
           student.save()

           # redirect to  students list
           return HttpResponseRedirect(reverse('home'))

        else:
            #render form width errors and previos user input
            return render(request, 'students/students_add.html',
                          {'groups' : Group.objects.all().order_by('title'),
                           'errors': errors})

    elif request.POST.get('cancel_button') is not None:
        # redirect to home page on cancel button
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request,'students/students_add.html',{'groups': Group.objects.all().order_by('title')})

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
