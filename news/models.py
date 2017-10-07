from ckeditor.fields import RichTextField
from django.db import models


class NewsCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    # сео мета теги
    meta_title = models.CharField(u'заголовок', max_length=150, blank=True)
    meta_keywords = models.CharField(u'ключевые слова', max_length=250, blank=True)
    meta_description = models.TextField(u'описание', blank=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория новости'
        verbose_name_plural = 'Категория новости'


class News(models.Model):
    title = models.CharField(max_length=120, verbose_name=u'Заголовок новости')
    slug = models.SlugField(max_length=200, verbose_name=u'Адрес', unique=True,
                            help_text=u'Адрес новости на латинице. Например, "your_address"')
    category = models.ForeignKey(NewsCategory, verbose_name=u'Категория', blank=True, null=True, default=None)

    content = RichTextField(verbose_name=u'Содержимое новости', blank=True)
    visible = models.BooleanField(u'отображать', default=True)

    # сео мета теги
    meta_title = models.CharField(u'заголовок', max_length=150, blank=True)
    meta_keywords = models.CharField(u'ключевые слова', max_length=250, blank=True)
    meta_description = models.TextField(u'описание', blank=True)

    created = models.DateTimeField(u'дата создания', auto_now_add=True, blank=True, null=True, editable=False)
    changed = models.DateTimeField(u'дата изменения', auto_now=True, blank=True, null=True, editable=False)

    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости'
        ordering = ['-created']

    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.get_absolute_url())

    def get_absolute_url(self):
        return u'news/%s/' % self.slug

    def save(self, **kwargs):
        self.title = self.title.strip()
        super(News, self).save(**kwargs)

    def get_title(self):
        return self.meta_title or self.title
