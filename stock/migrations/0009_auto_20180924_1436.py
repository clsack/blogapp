# Generated by Django 2.1 on 2018-09-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_auto_20180924_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hashtags',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Hashtags'),
        ),
    ]
