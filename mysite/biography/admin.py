from django.contrib import admin
from .models import MainPage, Otzivy


# Register your models here.


class MainPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'picture', 'picture_description')
    fields = ('picture', 'picture_description')


class OtzivAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'otziv', 'avatar')


admin.site.register(MainPage, MainPageAdmin)
admin.site.register(Otzivy, OtzivAdmin)
