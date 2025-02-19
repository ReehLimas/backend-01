from rest_framework.serializers import ModelSerializer
from .models import Cliente
from .models import Pedido
from .models import ItensProduto

class ClientesSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidosSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ItensProdutosSerializer(ModelSerializer):
    class Meta:
        model = ItensProduto
        fields = '__all__'