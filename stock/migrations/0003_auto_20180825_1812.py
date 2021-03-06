# Generated by Django 2.1 on 2018-08-25 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20180824_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Accesories', (('sheets', 'Sheets'), ('sponge', 'Sponge'))), ('Skin Care', (('bodycream', 'Body cream'), ('bodyscrub', 'Body scrub'), ('bodywash', 'Body wash'), ('eyecream', 'Eye cream'), ('facecream', 'Face cream'), ('faceprimer', 'Face primer'), ('facescrub', 'Face scrub'), ('handcream', 'Hand cream'), ('lipbalm', 'Lip balm'), ('makeupremover', 'Makeup remover'), ('mask', 'Mask'), ('serum', 'Serum'), ('shampoo', 'Shampoo'), ('soap', 'Soap'), ('sunblock', 'Sun block'), ('thermalwater', 'Thermal water'), ('toninglotion', 'Toning lotion'))), ('Nail Polish', (('basecoat', 'Base coat'), ('color', 'Color'), ('topcoat', 'Top coat'))), ('Make Up', (('blush', 'Blush'), ('bronzer', 'Bronzer'), ('brow', 'Brow'), ('concealer', 'Concealer'), ('eyeliner', 'Eye liner'), ('eyeprimer', 'Eye primer'), ('eyeshadowpds', 'Eye shadow palette Drugstore'), ('eyeshadowphe', 'Eye shadow palette High end'), ('eyeshadowsds', 'Eye shadow single Drugstore'), ('eyeshadowshe', 'Eye shadow single High end'), ('foundation', 'Foundation'), ('gloss', 'Gloss'), ('highlighter', 'Highlighter'), ('lipliner', 'Lip liner'), ('lipstick', 'Lipstick'), ('mascara', 'Mascara'), ('paletteds', 'Palette Drugstore'), ('palettehe', 'Palette High end'), ('powder', 'Powder'), ('tint', 'Tint'))), ('Parfum', (('bodysplash', 'Body splash'), ('toilette', 'Eau de Toilette'), ('parfum', 'Eau de Parfum')))], max_length=100, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, choices=[('beige', 'Beige'), ('black', 'Black'), ('blue', 'Blue'), ('bordeaux', 'Bordeaux'), ('brown', 'Brown'), ('clear', 'Clear'), ('copper', 'Copper'), ('gold', 'Gold'), ('green', 'Green'), ('grey', 'Grey'), ('lightblue', 'Lightblue'), ('mix', 'Mix'), ('orange', 'Orange'), ('pink', 'Pink'), ('red', 'Red'), ('silver', 'Silver'), ('violet', 'Violet'), ('white', 'White'), ('yellow', 'Yellow')], max_length=30, null=True, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='finish',
            field=models.CharField(blank=True, choices=[('crack', 'Crack'), ('creme', 'Creme'), ('cremeglitter', 'Creme glitter'), ('duochrome', 'Duochrome'), ('flakies', 'Flakies'), ('glassflecks', 'Glass flecks'), ('glitter', 'Glitter'), ('holographic', 'Holographic'), ('jelly', 'Jelly'), ('matte', 'Matte'), ('metal', 'Metal'), ('mirror', 'Mirror'), ('neon', 'Neon'), ('pearl', 'Pearl'), ('sandy', 'Sandy'), ('satin', 'Satin'), ('shimmer', 'Shimmer')], max_length=50, null=True, verbose_name='Finish'),
        ),
    ]
