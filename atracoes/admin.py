from django.contrib import admin
from django.utils.html import format_html

from .models import Atracao

class ListandoAtracoes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade_minima', 'thumbnail')

    def thumbnail(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="width: 50px"/>'.format(obj.foto.url))

    thumbnail.short_description = "Foto Ponto Turístico"


admin.site.register(Atracao, ListandoAtracoes)
