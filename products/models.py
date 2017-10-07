import datetime
import os

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from pytils.translit import translify, slugify


def FilePathPhotos(instance, filename):
    name, ext = os.path.splitext(translify(filename).replace(' ', '_'))
    hashed_name = name + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_name = hashed_name + ext
    return os.path.join('static/uploads', 'product_images', new_name)


class ProductCategory(MPTTModel):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=250, verbose_name=u'Адрес', unique=True,
                            help_text=u'Адрес категории на латинице. Например, "your_address"')
    category_image = models.ImageField(upload_to=FilePathPhotos, null=True, blank=True)
    meta_title = models.CharField(u'заголовок', max_length=150, blank=True)
    meta_keywords = models.CharField(u'ключевые слова', max_length=250, blank=True)
    meta_description = models.TextField(u'описание', blank=True)

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(u'дата создания', auto_now_add=True, blank=True, null=True, editable=False)
    changed = models.DateTimeField(u'дата изменения', auto_now=True, blank=True, null=True, editable=False)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
        ordering = ['-created']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return u'/%s/' % self.slug

    def get_title(self):
        if self.meta_title:
            return self.meta_title
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=250, verbose_name=u'Адрес', unique=True,
                            help_text=u'Адрес категории на латинице. Например, "your_address"')
    category = models.ForeignKey(ProductCategory, default=25, verbose_name=u'категория', blank=True, null=True)
    vendor_code = models.CharField(max_length=250, blank=True, null=False, default=None, verbose_name=u'Артикул', unique=True)
    price = models.FloatField(blank=True, null=False, default=0.00, verbose_name=u'Цена')
    old_price = models.FloatField(blank=True, null=False, default=0.00, verbose_name=u'Старая цена')
    discount_price = models.FloatField(blank=True, null=False, default=0.00, verbose_name=u'Скидочная цена')
    brand = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Бренд')
    weight = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'Вес')
    size = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'Размер')
    material = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'Материал')
    density = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'Плотность')
    source = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Имя магазина товара')

    meta_title = models.CharField(u'заголовок', max_length=150, blank=True)
    meta_keywords = models.CharField(u'ключевые слова', max_length=250, blank=True)
    meta_description = models.TextField(u'описание', blank=True)

    is_active = models.BooleanField(default=1)

    created = models.DateTimeField(u'дата создания', auto_now_add=True, blank=True, null=True, editable=False)
    changed = models.DateTimeField(u'дата изменения', auto_now=True, blank=True, null=True, editable=False)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to=FilePathPhotos)

    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
