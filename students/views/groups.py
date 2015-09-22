# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'Мтм-1',
         'leader': {'id': 1, 'name': u'Іванов Іван'}},
        {'id': 2,
         'name': u'Мтм-22',
         'leader': {'id': 2, 'name': u'Петрів Петро'}},
        {'id': 3,
         'name': u'Мтм-2',
         'leader': {'id': 3, 'name': u'Василів Василів'}},
    )

    return render(request, 'students/groups.html',
        {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
