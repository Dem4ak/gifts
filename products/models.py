import datetime
import os

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from pytils.translit import translify, slugify
from ckeditor.fields import RichTextField


def FilePathPhotos(instance, filename):
    name, ext = os.path.splitext(translify(filename).replace(' ', '_'))
    hashed_name = name + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_name = hashed_name + ext
    return os.path.join('static/uploads', 'product_images', new_name)


class Category(MPTTModel):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=250, verbose_name=u'Адрес', unique=True,
                            help_text=u'Адрес категории на латинице. Например, "your_address"')
    category_image = models.ImageField(upload_to=FilePathPhotos, null=True, blank=True)
    meta_title = models.CharField(u'заголовок', max_length=150, blank=True)
    meta_keywords = models.CharField(u'ключевые слова', max_length=250, blank=True)
    meta_description = models.TextField(u'описание', blank=True)

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    seo_text_top = RichTextField(verbose_name=u'Текст сверху страницы', blank=True)
    seo_text_bottom_left = RichTextField(verbose_name=u'Текст внизу слева', blank=True)
    seo_text_bottom_right = RichTextField(verbose_name=u'Текст внизу справа', blank=True)
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
        return u'/category/%s/' % self.slug

    def get_title(self):
        if self.meta_title:
            return self.meta_title
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    full_name = models.CharField(max_length=258, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=250, verbose_name=u'Адрес', unique=True,
                            help_text=u'Адрес категории на латинице. Например, "your_address"')
    description = models.TextField(verbose_name=u'Описание', null=True, default=None)
    category = models.ForeignKey(Category, verbose_name=u'Главная категории', blank=True)
    vendor_code = models.CharField(max_length=250,
                                   blank=True, null=False, default=None, verbose_name=u'Артикул', unique=True)
    price = models.FloatField(blank=True, null=False, default=0.00, verbose_name=u'Цена')
    discount_price = models.FloatField(blank=True, null=False, default=0.00, verbose_name=u'Скидочная цена')
    brand = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Бренд')
    branding = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Брендинг')
    size = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'Размер')
    material = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'Материал')
    source = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Имя магазина товара')

    meta_title = models.CharField(u'заголовок', max_length=150, blank=True)
    meta_keywords = models.CharField(u'ключевые слова', max_length=250, blank=True)
    meta_description = models.TextField(u'описание', blank=True)

    is_active = models.BooleanField(default=1)
    stock = models.IntegerField(blank=True, null=True, verbose_name=u'Количество товара')
    group_id = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'ID группы товаров')
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


class ProductColor(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    color = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Цвет')

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Цвет товара'
        verbose_name_plural = 'Цвета товаров'


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    name = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'Имя атрибута')
    value = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'Значение атрибута')
    dim = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'Величина атрибута')

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Атрибут товара'
        verbose_name_plural = 'Атрибуты товаров'


class ProductToCategory(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    category = models.ForeignKey(Category, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class ProductReview(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    name = models.CharField(max_length=128, blank=True, null=False, default=None, verbose_name=u'Имя')
    text = models.TextField(blank=True, verbose_name=u'Текст отзыва')
    rating = models.IntegerField(blank=True, verbose_name=u'Оценка отзыва', default=5)
    is_active = models.BooleanField(default=0, verbose_name=u'Отображать')

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Отзыв о товаре'
        verbose_name_plural = 'Отзывы'


