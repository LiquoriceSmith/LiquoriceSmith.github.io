from django.db import models


# Create your models here.


class MainPage(models.Model):
    picture = models.ImageField(verbose_name='Фото', blank='True')
    picture_description = models.CharField(max_length=150, verbose_name='Описание картины')
    picture_data = models.DateTimeField(blank=True)
