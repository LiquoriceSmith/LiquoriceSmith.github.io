from django.contrib import admin
from .models import MainPage


# Register your models here.


class MainPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'picture', 'picture_description', 'picture_data')
    fields = ('picture', 'picture_description', 'picture_data')


admin.site.register(MainPage, MainPageAdmin)
