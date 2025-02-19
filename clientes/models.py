from django.db import models

class Cliente(models.Model):
    id = models.primary_key = True
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.nome}"

class Pedido(models.Model):
    id = models.primary_key = True
    valor_total = models.CharField(max_length=50)
    pedido = models.CharField(max_length=50)
    data_pedido = models.DateField(max_length=8)
    
    def __str__(self):
        return f"{self.id}"
    
class ItensProduto(models.Model):
    quantidade = models.BinaryField(max_length=7)
    preco_unitario= models.BinaryField(max_length=50)
    produto = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.quantidade}"