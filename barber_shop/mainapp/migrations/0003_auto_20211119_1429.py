# Generated by Django 3.2.9 on 2021-11-19 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20211119_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='photo',
            field=models.ImageField(upload_to='uploads/masters', verbose_name='Фото мастера'),
        ),
        migrations.AlterField(
            model_name='service',
            name='photo',
            field=models.ImageField(upload_to='uploads/service', verbose_name='Фото'),
        ),
    ]
