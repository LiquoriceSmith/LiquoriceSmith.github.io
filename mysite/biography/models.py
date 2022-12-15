from django.db import models


# Create your models here.


class MainPage(models.Model):
    picture = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank='True')
    picture_description = models.CharField(max_length=150, verbose_name='Описание картины', blank='True')

    def __str__(self):
        return self.picture_description

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Otzivy(models.Model):
    name = models.CharField(max_length=250, verbose_name='Как вас зовут?')
    otziv = models.TextField(blank=True, verbose_name='Ваш отзыв')
    data = models.DateTimeField(auto_now=True, verbose_name='Дата отзыва')
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Выберите фото для аватара', blank='True')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
