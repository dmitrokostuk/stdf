# _*_ coding: utf-8 _*_
from django.db import models

# Create your models here.




class Group(models.Model):
    """Group Model"""

    class Meta(object):
        verbose_name = u"Група"
        verbose_name_plural = u"Групи"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва")

    raports = models.TextField(
        max_length=256,
        blank=True,
        verbose_name=u"Рапорти на групу"
    )

    leader = models.OneToOneField('Student',
        verbose_name=u"Староста",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)


    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    def __unicode__(self):
        if self.leader:
            return u"%s (%s %s)" % (self.title, self.leader.first_name,
                 self.leader.last_name)
        else:
            return u"%s" % (self.title,)


