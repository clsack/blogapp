from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    product = models.CharField(max_length=100, verbose_name='Product')
    brand = models.CharField(max_length=100, verbose_name='Brand')
    collection = models.CharField(max_length=100, verbose_name='Collection')
    category = models.CharField(choices=CATEGORY)
    finish = models.CharField(choices=FINISH)
    color = models.CharField(choices=COLOR)
    brought_date = models.DateField()
    expiration_date = models.DateField()
    currency = models.CharField(max_length=3, choices=CURRENCY, default=ARS)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    posted = models.BooleanField()
    percentage_used = models.FloatField()
    finished = models.BooleanField()
    picture = models.ImageField

    class Meta:
        ordering = ['date_from']
        get_latest_by = ['-date_from']

    def __str__(self):
        return self.event_text

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    brand = models.CharField(max_length=100, verbose_name='Title')
    product = models.ForeignKey(
            'Product',
            on_delete=models.CASCADE,
    )
    link = models.URLField(max_length=200)
    short = models.URLField(max_length=50)
    date = models.DateField()
    gr = models.BooleanField()
    fb = models.BooleanField()
    tw = models.BooleanField()
    pi = models.BooleanField()
    ig = models.BooleanField()
    co = models.BooleanField()

    class Meta:
        ordering = ['date_scheduled']
        get_latest_by = ['-date_scheduled']

    def __str__(self):
        return self.task_text

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})
