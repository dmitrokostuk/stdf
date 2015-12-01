# -*- coding: utf-8 -*-

from django.shortcuts import  render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from studentsdb.studdb.settings import ADMIN_EMAIL

class ContactForm(forms.Form):

    from_email = forms.EmailField(
        label=u"Your email",
    )

    subject = forms.CharField(
        label=u"Заголовок листа",
        max_length=128)

    message = forms.CharField(
        label=u"Текст Повідомлення",
        max_length=1024,
        widget=forms.Textarea
    )
def contact_admin(request):
    # check if form was posted
    if request.method == 'POST':
        #create a form instatce and populate it width data request:
        form = ContactForm(request.POST)
        #check whether user data is valid
        if form.is_valid():
            #send email
            subject = form.clened_data['subject']
            message = form.clened_data['message']
            from_email = form.clened_data['from_email']

            try:
                send_mail(subject,message,from_email,[ADMIN_EMAIL])
            except Exception:
                message = u"Під час відсилання листа сталася помилка,скористайтесь формою пізніше"
        else:
            message = u"Форма успішно надіслана"
        #redirect to same contact page width sucsess message
        return HttpResponseRedirect(
            u'%s?status_message=%s' % (reverse('contact_admin'),message)
        )
    #if there was not POST render blank form
    else:
        form = ContactForm()

    return render(request, 'contact_admin/form.html', {})