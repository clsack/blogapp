from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

from .constants import CATEGORY, FINISH, COLOR, CURRENCY, QUALITY
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
    posted = models.BooleanField(verbose_name='Posted',
                                 default=False)
    picture = models.ImageField(blank=True,
                                null=True)

    class Meta:
        ordering = ['product', 'brand', 'category']

    def __str__(self):
        return self.product

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})


class Post(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Title')
    brand = models.CharField(max_length=100,
                             verbose_name='Brand')
    product = models.ManyToManyField(Product,
                                     verbose_name='Product')
    tags = models.CharField(max_length=200,
                            verbose_name='Tags')
    hashtags = models.CharField(max_length=200,
                                verbose_name='Hashtags')
    status = models.CharField(max_length=10,
                              verbose_name='Status')
    link = models.URLField(max_length=200,
                           verbose_name='Link',
                           null=True)
    short = models.URLField(max_length=50,
                            verbose_name='Short link',
                            null=True)
    date = models.DateField(verbose_name='Posted date',
                            null=True)
    ig = models.BooleanField(verbose_name='Published on Instagram')
    co = models.BooleanField(verbose_name='Comments replied')

    class Meta:
        ordering = ['-date']
        get_latest_by = ['-date']

    def __str__(self):
        return self.task_text

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def clean(self):
        if self.hashtags == '':
            self.hashtags = generate_hashtags(self.product)
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError(_('Drafts may not have a publication date.'))
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()
