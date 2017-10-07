import datetime
import os
from pytils.translit import translify
from ckeditor.fields import RichTextField
from django.db import models


def FilePathPhotos(instance, filename):
    name, ext = os.path.splitext(translify(filename).replace(' ', '_'))
    hashed_name = name + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_name = hashed_name + ext
    return os.path.join('static/uploads', 'slider_images', new_name)


class Home(models.Model):
    title = models.CharField(max_length=120, verbose_name=u'Заголовок страницы')
    seo_text = RichTextField(verbose_name=u'Сео текст на главной', blank=True)
    # сео мета теги
    meta_title = models.CharField(u'заголовок', max_length=150, blank=True)
    meta_keywords = models.CharField(u'ключевые слова', max_length=250, blank=True)
    meta_description = models.TextField(u'описание', blank=True)

    class Meta:
        verbose_name = u'Главная страница'
        verbose_name_plural = u'Главная страница'


class SliderImage(models.Model):
    key = models.ForeignKey(Home, blank=True, null=True, default=None)
    image = models.ImageField(upload_to=FilePathPhotos)
    alt = models.CharField(max_length=128, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class StepBy(models.Model):
    title = models.CharField(max_length=120, verbose_name=u'Заголовок шага', blank=True, null=True, default=None)
    content = RichTextField(verbose_name=u'Текст шага', blank=True)
    sort = models.IntegerField(verbose_name=u'Номер шага', default=10)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Шаг оформления'
        verbose_name_plural = 'Шаги оформления'