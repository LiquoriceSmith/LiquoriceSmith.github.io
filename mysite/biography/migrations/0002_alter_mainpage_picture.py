# Generated by Django 4.1.2 on 2022-10-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='picture',
            field=models.ImageField(blank='True', upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
