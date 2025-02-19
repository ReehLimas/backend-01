from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from clientes.views import ClientesViewSet
from clientes.views import PedidosViewSet
from clientes.views import ItensProdutosViewSet


router = DefaultRouter()
router.register('clientes', ClientesViewSet)
router.register('pedidos', PedidosViewSet)
router.register('itens', ItensProdutosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]