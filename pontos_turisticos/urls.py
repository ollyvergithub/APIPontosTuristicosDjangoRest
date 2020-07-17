from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
# Autenticação
from rest_framework.authtoken.views import obtain_auth_token

from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet

router = routers.DefaultRouter()
# basename='PontoTuristico', foi necessário pelo override na class PontoTuristicoViewSet(ModelViewSet): - def get_queryset(self):
router.register(r'pontosturisticos', PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'atracoes', AtracaoViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # API
    path('api/', include(router.urls)),
    # Autenticacao
    path('api-token-auth/', obtain_auth_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
