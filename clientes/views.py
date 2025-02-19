from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Cliente
from .models import Pedido
from .models import ItensProduto
from .serializers import ClientesSerializer
from .serializers import PedidosSerializer
from .serializers import ItensProdutosSerializer

class ClientesViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

class PedidosViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidosSerializer

class ItensProdutosViewSet(ModelViewSet):
    queryset = ItensProduto.objects.all()
    serializer_class = ItensProdutosSerializer
