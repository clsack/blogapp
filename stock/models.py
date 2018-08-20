from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

# Create your models here.


class Product(models.Model):
    CATEGORY = (
        ('Accesories', (
                ('sheets', 'Sheets'),
                ('sponge', 'Sponge'),
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
                ('toninglotion', 'Toning lotion'),
                )),
        ('Nail Polish', (
                ('basecoat', 'Base coat'),
                ('color', 'Color'),
                ('topcoat', 'Top coat'),
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
                ('eyeshadowsds', 'Eye shadow single Drugstore'),
                ('eyeshadowshe', 'Eye shadow single High end'),
                ('foundation', 'Foundation'),
                ('gloss', 'Gloss'),
                ('highlighter', 'Highlighter'),
                ('lipliner', 'Lip liner'),
                ('lipstick', 'Lipstick'),
                ('mascara', 'Mascara'),
                ('paletteds', 'Palette Drugstore'),
                ('palettehe', 'Palette High end'),
                ('powder', 'Powder'),
                ('tint', 'Tint'),
                )),
        ('Parfum', (
                ('bodysplash', 'Body splash'),
                ('toilette', 'Eau de Toilette'),
                ('parfum', 'Eau de Parfum'),
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
    QUALITY = (
        ('5', 'Excellent'),
        ('4', 'Really good'),
        ('3', 'Good'),
        ('2', 'Poor'),
        ('1', 'Awful')
    )
    product = models.CharField(max_length=150, verbose_name='Product')
    brand = models.CharField(max_length=100, verbose_name='Brand')
    collection = models.CharField(max_length=100,
                                  verbose_name='Collection',
                                  null=True)
    category = models.CharField(max_length=100, choices=CATEGORY, verbose_name='Category')
    finish = models.CharField(max_length=50, choices=FINISH, verbose_name='Finish')
    color = models.CharField(max_length=30, choices=COLOR, verbose_name='Color')
    bought_date = models.DateField(verbose_name='Bought date')
    expiration_date = models.DateField(verbose_name='Expiration date')
    currency = models.CharField(max_length=3,
                                choices=CURRENCY,
                                verbose_name='Currency',
                                null=True)
    price = models.DecimalField(max_digits=7,
                                decimal_places=2,
                                verbose_name='Price',
                                null=True)
    duration = models.CharField(max_length=20, choices=QUALITY,
                                verbose_name='Duration',
                                null=True)
    quality = models.CharField(max_length=20, choices=QUALITY,
                               verbose_name='Quality',
                               null=True)
    project_pan = models.BooleanField(verbose_name='Project pan')
    percentage_used = models.IntegerField(default=1,
                                          validators=[
                                                  MaxValueValidator(100),
                                                  MinValueValidator(0)
                                                  ],
                                          verbose_name='Percentage used')
    finished = models.BooleanField(verbose_name='Finished', null=True)
    posted = models.BooleanField(verbose_name='Posted', null=True)
    picture = models.ImageField()

    class Meta:
        ordering = ['product', 'brand', 'category']

    def __str__(self):
        return self.event_text

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    brand = models.CharField(max_length=100, verbose_name='Brand')
    product = models.ManyToManyField(Product, verbose_name='Product')
    tags = models.CharField(max_length=200, verbose_name='Tags')
    hashtags = models.CharField(max_length=200, verbose_name='Hashtags')
    posted = models.BooleanField(verbose_name='Posted')
    link = models.URLField(max_length=200, verbose_name='Link', null=True)
    short = models.URLField(max_length=50,
                            verbose_name='Short link',
                            null=True)
    date = models.DateField(verbose_name='Posted date', null=True)
    ig = models.BooleanField(verbose_name='Published on Instagram')
    co = models.BooleanField(verbose_name='Comments replied')

    class Meta:
        ordering = ['-date']
        get_latest_by = ['-date']

    def __str__(self):
        return self.task_text

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
