from django.db import models
import datetime
import os
from pytils.translit import translify


def FilePathPhotos(instance, filename):
    name, ext = os.path.splitext(translify(filename).replace(' ', '_'))
    hashed_name = name + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_name = hashed_name + ext
    return os.path.join('static/uploads', 'our_works', new_name)


class Works(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True, default=None)
    created = models.DateTimeField(u'дата создания', auto_now_add=True, blank=True, null=True, editable=False)
    changed = models.DateTimeField(u'дата изменения', auto_now=True, blank=True, null=True, editable=False)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


class WorksImage(models.Model):
    work = models.ForeignKey(Works, blank=True, null=True, default=None)
    is_big = models.BooleanField(blank=True, default=False)
    image = models.ImageField(upload_to=FilePathPhotos)

    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фото работы'
        verbose_name_plural = 'Фото работ'