from django.contrib import admin

from django.contrib import admin
from .models import Cliente
from .models import Pedido
from .models import ItensProduto

admin.site.register(ItensProduto)
admin.site.register(Pedido)
admin.site.register(Cliente)
