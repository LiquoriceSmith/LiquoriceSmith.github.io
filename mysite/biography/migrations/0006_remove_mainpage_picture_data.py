# Generated by Django 4.1.2 on 2022-12-15 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0005_alter_otzivy_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainpage',
            name='picture_data',
        ),
    ]
