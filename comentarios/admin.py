from django.contrib import admin
from .models import Comentario
from .actions_personalizadas import reprova_comentarios, aprova_comentarios


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'aprovado']
    list_editable = ('aprovado',)

    # Passando as actions personalizadas
    actions = [
        aprova_comentarios,
        reprova_comentarios,
    ]


admin.site.register(Comentario, ComentarioAdmin)
