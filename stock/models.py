from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    CATEGORY = (
        ('Accesories', (
                ('sheets', 'Sheets'),
                ('sponge', 'Sponge')
                )),
        ('Skin Care', (
                ('bodycream', 'Body cream'),
                ('bodyscrub', 'Body scrub'),
                ('bosywash', 'Body wash'),
                ('eyecream', 'Eye cream'),
                ('facecream', 'Face cream'),
                ('faceprimer', 'Face primer'),
                ('facescrub', 'Face scrub'),
                ('handcream', 'Hand cream'),
                ('lipbalm', 'Lip balm'),
                ('makeupremover', 'Makeup remover'),
                ('mask', 'Mask'),
                ('serum', 'Serum'),
                ('shampoo', 'Shampoo'),
                ('soap', 'Soap'),
                ('sunblock', 'Sun block'),
                ('thermalwater', 'Thermal water'),
                ('toninglotion', 'Toning lotion')
                )),
        ('Nail Polish', (
                ('basecoat', 'Base coat'),
                ('color', 'Color'),
                ('topcoat', 'Top coat')
                )),
        ('Make Up', (
                ('blush', 'Blush'),
                ('bronzer', 'Bronzer'),
                ('brow', 'Brow'),
                ('concealer', 'Concealer'),
                ('eyeliner', 'Eye liner'),
                ('eyeprimer', 'Eye primer'),
                ('eyeshadowpds', 'Eye shadow palette Drugstore'),
                ('eyeshadowphe', 'Eye shadow palette High end'),
                ('eyeshadowsds', 'Eye shadow Single Drugstore'),
                ('eyeshadowshe', 'Eye shadow Single High end'),
                ('foundation', 'Foundation'),
                ('gloss', 'Gloss'),
                ('highlighter', 'Highlighter'),
                ('lipliner', 'Lip liner'),
                ('lipstick', 'Lipstick'),
                ('mascara', 'Mascara'),
                ('paletteds', 'Palette Drugstore'),
                ('palettehe', 'Palette High end'),
                ('powder', 'Powder'),
                ('tint', 'Tint')
                ))
        ('Parfum', (
                ('bodysplash', 'Body splash'),
                ('toilette', 'Eau de Toilette'),
                ('parfum', 'Eau de Parfum')
                )),
    )
    FINISH = (
        ('crack', 'Crack'),
        ('creme', 'Creme'),
        ('cremeglitter', 'Creme glitter'),
        ('duochrome', 'Duochrome'),
        ('flakies', 'Flakies'),
        ('glassflecks', 'Glass flecks'),
        ('glitter', 'Glitter'),
        ('holographic', 'Holographic'),
        ('jelly', 'Jelly'),
        ('matte', 'Matte'),
        ('metal', 'Metal'),
        ('mirror', 'Mirror'),
        ('neon', 'Neon'),
        ('pearl', 'Pearl'),
        ('sandy', 'Sandy'),
        ('satin', 'Satin'),
        ('shimmer', 'Shimmer'),
    )
    COLOR = (
        ('beige', 'Beige'),
        ('black', 'Black'),
        ('blue', 'Blue'),
        ('bordeaux', 'Bordeaux'),
        ('brown', 'Brown'),
        ('clear', 'Clear'),
        ('copper', 'Copper'),
        ('gold', 'Gold'),
        ('green', 'Green'),
        ('grey', 'Grey'),
        ('lightblue', 'Lightblue'),
        ('mix', 'Mix'),
        ('orange', 'Orange'),
        ('pink', 'Pink'),
        ('red', 'Red'),
        ('silver', 'Silver'),
        ('violet', 'Violet'),
        ('white', 'White'),
        ('yellow', 'Yellow')
    )
    CURRENCY = (
        ('ARS', 'Argentina Peso'),
        ('BRL', 'Brazil Real'),
        ('CLP', 'Chilean Peso'),
        ('USD', 'United States Dollar'),
        ('UYU', 'Uruguay Peso')
    )
    product = models.CharField(max_length=100, verbose_name='Product')
    brand = models.CharField(max_length=100, verbose_name='Brand')
    collection = models.CharField(max_length=100, verbose_name='Collection')
    category = models.CharField(choices=CATEGORY, verbose_name='Category')
    finish = models.CharField(choices=FINISH, verbose_name='Finish')
    color = models.CharField(choices=COLOR, verbose_name='Color')
    brought_date = models.DateField(verbose_name='Brought date')
    expiration_date = models.DateField(verbose_name='Expiration date')
    currency = models.CharField(max_length=3, choices=CURRENCY, verbose_name='Currency')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price')
    posted = models.BooleanField(verbose_name='Posted?')
    percentage_used = models.FloatField(verbose_name='Percentage used')
    finished = models.BooleanField(verbose_name='Finished?')
    picture = models.ImageField()

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
