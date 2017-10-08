from ckeditor.fields import RichTextField
from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=120, verbose_name=u'Заголовок страницы')
    slug = models.SlugField(max_length=200, verbose_name=u'Адрес', unique=True,
                            help_text=u'Адрес страницы на латинице. Например, "your_address"')

    content = RichTextField(verbose_name=u'Содержимое страницы', blank=True)

    order = models.IntegerField(verbose_name=u'Порядок сортировки', default=10)
    template = models.CharField(verbose_name=u'шаблон', max_length=100, default=u'default.html')
    visible = models.BooleanField(u'отображать', default=True)

    # сео мета теги
    meta_title = models.CharField(u'заголовок', max_length=150, blank=True)
    meta_keywords = models.CharField(u'ключевые слова', max_length=250, blank=True)
    meta_description = models.TextField(u'описание', blank=True)

    created = models.DateTimeField(u'дата создания', auto_now_add=True, blank=True, null=True, editable=False)
    changed = models.DateTimeField(u'дата изменения', auto_now=True, blank=True, null=True, editable=False)

    class Meta:
        verbose_name = u'страница'
        verbose_name_plural = u'страницы'

    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.get_absolute_url())

    def get_absolute_url(self):
        return u'/page/%s/' % self.slug

    def save(self, **kwargs):
        self.title = self.title.strip()
        super(Page, self).save(**kwargs)

    def get_title(self):
        return self.meta_title or self.title