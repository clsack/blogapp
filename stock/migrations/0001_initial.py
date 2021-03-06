# Generated by Django 2.1 on 2018-08-24 20:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('brand', models.CharField(max_length=100, verbose_name='Brand')),
                ('tags', models.CharField(max_length=200, verbose_name='Tags')),
                ('hashtags', models.CharField(max_length=200, verbose_name='Hashtags')),
                ('posted', models.BooleanField(verbose_name='Posted')),
                ('link', models.URLField(null=True, verbose_name='Link')),
                ('short', models.URLField(max_length=50, null=True, verbose_name='Short link')),
                ('date', models.DateField(null=True, verbose_name='Posted date')),
                ('ig', models.BooleanField(verbose_name='Published on Instagram')),
                ('co', models.BooleanField(verbose_name='Comments replied')),
            ],
            options={
                'ordering': ['-date'],
                'get_latest_by': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=150, verbose_name='Product')),
                ('brand', models.CharField(max_length=100, verbose_name='Brand')),
                ('collection', models.CharField(max_length=100, null=True, verbose_name='Collection')),
                ('category', models.CharField(choices=[('Accesories', (('sheets', 'Sheets'), ('sponge', 'Sponge'))), ('Skin Care', (('bodycream', 'Body cream'), ('bodyscrub', 'Body scrub'), ('bosywash', 'Body wash'), ('eyecream', 'Eye cream'), ('facecream', 'Face cream'), ('faceprimer', 'Face primer'), ('facescrub', 'Face scrub'), ('handcream', 'Hand cream'), ('lipbalm', 'Lip balm'), ('makeupremover', 'Makeup remover'), ('mask', 'Mask'), ('serum', 'Serum'), ('shampoo', 'Shampoo'), ('soap', 'Soap'), ('sunblock', 'Sun block'), ('thermalwater', 'Thermal water'), ('toninglotion', 'Toning lotion'))), ('Nail Polish', (('basecoat', 'Base coat'), ('color', 'Color'), ('topcoat', 'Top coat'))), ('Make Up', (('blush', 'Blush'), ('bronzer', 'Bronzer'), ('brow', 'Brow'), ('concealer', 'Concealer'), ('eyeliner', 'Eye liner'), ('eyeprimer', 'Eye primer'), ('eyeshadowpds', 'Eye shadow palette Drugstore'), ('eyeshadowphe', 'Eye shadow palette High end'), ('eyeshadowsds', 'Eye shadow single Drugstore'), ('eyeshadowshe', 'Eye shadow single High end'), ('foundation', 'Foundation'), ('gloss', 'Gloss'), ('highlighter', 'Highlighter'), ('lipliner', 'Lip liner'), ('lipstick', 'Lipstick'), ('mascara', 'Mascara'), ('paletteds', 'Palette Drugstore'), ('palettehe', 'Palette High end'), ('powder', 'Powder'), ('tint', 'Tint'))), ('Parfum', (('bodysplash', 'Body splash'), ('toilette', 'Eau de Toilette'), ('parfum', 'Eau de Parfum')))], max_length=100, verbose_name='Category')),
                ('finish', models.CharField(choices=[('crack', 'Crack'), ('creme', 'Creme'), ('cremeglitter', 'Creme glitter'), ('duochrome', 'Duochrome'), ('flakies', 'Flakies'), ('glassflecks', 'Glass flecks'), ('glitter', 'Glitter'), ('holographic', 'Holographic'), ('jelly', 'Jelly'), ('matte', 'Matte'), ('metal', 'Metal'), ('mirror', 'Mirror'), ('neon', 'Neon'), ('pearl', 'Pearl'), ('sandy', 'Sandy'), ('satin', 'Satin'), ('shimmer', 'Shimmer')], max_length=50, verbose_name='Finish')),
                ('color', models.CharField(choices=[('beige', 'Beige'), ('black', 'Black'), ('blue', 'Blue'), ('bordeaux', 'Bordeaux'), ('brown', 'Brown'), ('clear', 'Clear'), ('copper', 'Copper'), ('gold', 'Gold'), ('green', 'Green'), ('grey', 'Grey'), ('lightblue', 'Lightblue'), ('mix', 'Mix'), ('orange', 'Orange'), ('pink', 'Pink'), ('red', 'Red'), ('silver', 'Silver'), ('violet', 'Violet'), ('white', 'White'), ('yellow', 'Yellow')], max_length=30, verbose_name='Color')),
                ('bought_date', models.DateField(blank=True, null=True, verbose_name='Bought date')),
                ('expiration_date', models.CharField(max_length=3, verbose_name='Expiration date')),
                ('currency', models.CharField(choices=[('ARS', 'Argentina Peso'), ('BRL', 'Brazil Real'), ('CLP', 'Chilean Peso'), ('USD', 'United States Dollar'), ('UYU', 'Uruguay Peso')], max_length=3, null=True, verbose_name='Currency')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='Price')),
                ('duration', models.CharField(choices=[('5', 'Excellent'), ('4', 'Really good'), ('3', 'Good'), ('2', 'Poor'), ('1', 'Awful')], max_length=20, null=True, verbose_name='Duration')),
                ('quality', models.CharField(choices=[('5', 'Excellent'), ('4', 'Really good'), ('3', 'Good'), ('2', 'Poor'), ('1', 'Awful')], max_length=20, null=True, verbose_name='Quality')),
                ('project_pan', models.BooleanField(verbose_name='Project pan')),
                ('percentage_used', models.IntegerField(default=0.0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Percentage used')),
                ('finished', models.BooleanField(default=False, verbose_name='Finished')),
                ('posted', models.BooleanField(default=False, verbose_name='Posted')),
                ('picture', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'ordering': ['product', 'brand', 'category'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='product',
            field=models.ManyToManyField(to='stock.Product', verbose_name='Product'),
        ),
    ]
