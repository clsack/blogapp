# Generated by Django 2.1 on 2018-09-25 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0014_auto_20180925_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('0', 'Draft'), ('1', 'Published')], default='Draft', max_length=10, verbose_name='Status'),
        ),
    ]
