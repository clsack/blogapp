# Generated by Django 2.1 on 2018-09-27 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0020_auto_20180925_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Accesories', (('buffer', 'Buffer'), ('brush', 'Brush'), ('sheets', 'Sheets'), ('sponge', 'Sponge'), ('stampingplate', 'Stamping plate'))), ('Skin Care', (('bodycream', 'Body cream'), ('bodyscrub', 'Body scrub'), ('bodywash', 'Body wash'), ('eyecream', 'Eye cream'), ('facecream', 'Face cream'), ('faceprimer', 'Face primer'), ('facescrub', 'Face scrub'), ('handcream', 'Hand cream'), ('lipbalm', 'Lip balm'), ('makeupremover', 'Makeup remover'), ('mask', 'Mask'), ('serum', 'Serum'), ('shampoo', 'Shampoo'), ('soap', 'Soap'), ('sunblock', 'Sun block'), ('thermalwater', 'Thermal water'), ('toninglotion', 'Toning lotion'))), ('Nail Polish', (('basecoat', 'Base coat'), ('color', 'Color'), ('topcoat', 'Top coat'))), ('Make Up', (('blush', 'Blush'), ('bronzer', 'Bronzer'), ('brow', 'Brow'), ('concealer', 'Concealer'), ('eyeliner', 'Eye liner'), ('eyeprimer', 'Eye primer'), ('eyeshadowpds', 'Eye shadow palette Drugstore'), ('eyeshadowphe', 'Eye shadow palette High end'), ('eyeshadowsds', 'Eye shadow single Drugstore'), ('eyeshadowshe', 'Eye shadow single High end'), ('foundation', 'Foundation'), ('gloss', 'Gloss'), ('highlighter', 'Highlighter'), ('lipliner', 'Lip liner'), ('lipstick', 'Lipstick'), ('mascara', 'Mascara'), ('paletteds', 'Palette Drugstore'), ('palettehe', 'Palette High end'), ('powder', 'Powder'), ('tint', 'Tint'))), ('Parfum', (('bodysplash', 'Body splash'), ('toilette', 'Eau de Toilette'), ('parfum', 'Eau de Parfum'))), ('Stationery', (('eraser', 'Eraser'), ('highlighter', 'Highlighter'), ('legalpad', 'Legal pad'), ('messagepad', 'Message pad'), ('notepad', 'Note pad'), ('pen', 'Pen'), ('postit', 'Post it'), ('stationery', 'Stationery'))), ('Other', (('empties', 'Empties'), ('projectpan', 'Project pan')))], max_length=100, verbose_name='Category'),
        ),
    ]