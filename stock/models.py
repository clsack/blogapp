from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

from datetime import datetime
import urllib
import os
from django.conf import settings
from .constants import CATEGORY, FINISH, COLOR, CURRENCY, QUALITY, STATUS
from .constants import GENERIC_LIST, PROJECTPAN_LIST, NAILS_LIST, NAILPOLISH_LIST
from .utils import generate_hashtags
# Create your models here.


class Product(models.Model):
    product = models.CharField(max_length=150,
                               verbose_name='Product')
    brand = models.CharField(max_length=100,
                             verbose_name='Brand')
    collection = models.CharField(max_length=100,
                                  verbose_name='Collection',
                                  blank=True,
                                  null=True)
    category = models.CharField(max_length=100,
                                choices=CATEGORY,
                                verbose_name='Category')
    finish = models.CharField(max_length=50,
                              choices=FINISH,
                              verbose_name='Finish',
                              blank=True,
                              null=True)
    color = models.CharField(max_length=30,
                             choices=COLOR,
                             verbose_name='Color',
                             blank=True,
                             null=True)
    bought_date = models.DateField(verbose_name='Bought date',
                                   blank=True,
                                   null=True)
    expiration_date = models.CharField(max_length=3,
                                       verbose_name='Expiration date')
    currency = models.CharField(max_length=3,
                                choices=CURRENCY,
                                verbose_name='Currency',
                                blank=True,
                                null=True)
    price = models.DecimalField(max_digits=7,
                                decimal_places=2,
                                verbose_name='Price',
                                blank=True,
                                null=True)
    duration = models.CharField(max_length=20, choices=QUALITY,
                                verbose_name='Duration',
                                blank=True,
                                null=True)
    quality = models.CharField(max_length=20, choices=QUALITY,
                               verbose_name='Quality',
                               blank=True,
                               null=True)
    project_pan = models.BooleanField(verbose_name='Project pan')
    percentage_used = models.IntegerField(default=0.0,
                                          validators=[
                                                  MaxValueValidator(100),
                                                  MinValueValidator(0)
                                                  ],
                                          verbose_name='Percentage used')
    finished = models.BooleanField(verbose_name='Finished',
                                   default=False)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              verbose_name='Status',
                              default='Draft')
    upload_path = 'media/product'
    image = models.ImageField(upload_to=upload_path, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['product', 'brand', 'category']

    def __str__(self):
        return self.product

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.image_url:
            file_save_dir = self.upload_path
            filename = urllib.parse(self.image_url).path.split('/')[-1]
            urllib.urlretrieve(self.image_url,
                               os.path.join(file_save_dir, filename))
            self.image = os.path.join(file_save_dir, filename)
            self.image_url = ''
            self.brand = filename.split('_')[0]
        super(Product, self).save()


class Post(models.Model):
    blogger_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100,
                             verbose_name='Title')
    brand = models.CharField(max_length=100,
                             verbose_name='Brand')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name='Product',
                                null=True)
    tags = models.CharField(max_length=300,
                            verbose_name='Tags',
                            null=True)
    hashtags = models.CharField(max_length=300,
                                verbose_name='Hashtags',
                                null=True,
                                blank=True)
    link = models.URLField(max_length=200,
                           verbose_name='Link')
    date = models.DateField(verbose_name='Posted date',
                            null=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              verbose_name='Status',
                              default='Draft')
    ig = models.BooleanField(verbose_name='Published on IG',
                             default=False)
    co = models.BooleanField(verbose_name='Comments replied',
                             default=False)
    upload_path = 'media/post'
    image = models.ImageField(upload_to=upload_path, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['-date']
        get_latest_by = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def clean(self):
        if getattr(self, 'hashtags', None) is None:
            if any(ext in self.title for ext in ['Project', 'Terminados', 'Empties']):
                self.hashtags = 'Project Pan update! ' + GENERIC_LIST + PROJECTPAN_LIST
            elif 'Nail Art' in self.title:
                self.hashtags = GENERIC_LIST + ' #'.join(NAILPOLISH_LIST) + NAILS_LIST
            else:
                self.hashtags = generate_hashtags(self.product)
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError('Drafts may not have a publication date.')
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()
