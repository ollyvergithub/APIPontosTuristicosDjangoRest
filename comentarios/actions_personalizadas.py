def reprova_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=False)


def aprova_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=True)


reprova_comentarios.short_description = "Reprova Comentários - Action Personalizada"
aprova_comentarios.short_description = "Aprova Comentários - Action Personalizada"
