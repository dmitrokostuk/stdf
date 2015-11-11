# _*_ coding: utf-8 _*_
from django.db import models

# Create your models here.

class Tests(models.Model):
    class Meta(object):
        verbose_name = u"Екзамен"
        verbose_name_plural = u"Екзамени"

    groupexams = models.ForeignKey('Group',
        verbose_name=u'Група',
        blank=False,
        null=True,
        on_delete=models.PROTECT
    )

    exam_title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва екзамену ",
        null=True

    )

    teacher = models.CharField(
        verbose_name=u"Викладач",
        max_length=256,
        blank=False,
        null=True
        )

    examtime = models.DateField(
        blank=False,
        verbose_name=u"Дата екзамену ",
        null=True
        )

    clasroom = models.CharField(
        verbose_name=u"Аудиторія",
        max_length=256,
        blank=False,
        null=True
    )
    notes = models.TextField(
        blank=True,
        verbose_name=u"Нотатки",
        null=True,
    )

    def __unicode__(self):
        return u"%s %s %s %s %s %s" %(self.groupexams,self.exam_title,self.teacher,self.examtime,self.clasroom,self.notes)
