from django.db import models


class Menu(models.Model):
    title = models.CharField(u'название', max_length=50)
    url = models.CharField(u'url', max_length=75)
    visible = models.BooleanField(u'отображать', default=True)
    order = models.IntegerField(u'порядок сортировки', default=10)

    class Meta:
        verbose_name = u'меню'
        verbose_name_plural = u'меню'
        ordering = ['order', 'pk']

    def __unicode__(self):
        return self.title
