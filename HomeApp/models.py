from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Toner(models.Model):
    descricao = models.CharField(max_length=200)
    referencia = models.CharField(max_length=200)
    cor = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s %s" % (self.descricao, self.referencia, self.cor)

class Departamento(models.Model):
    nome = models.CharField(max_length=200)
    responsavel = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % (self.nome)

class Entrada(models.Model):
    descricao = models.ForeignKey(Toner, on_delete=models.CASCADE)
    quantidade_entrada = models.IntegerField(default=1)
    data = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return "%s %s" % (self.descricao.descricao, self.descricao.referencia)

    datetime.timedelta(days=1)

    def entrada_recente(self):
        return self.data >= timezone.now()

    datetime

    class Meta:
        ordering = ['descricao']

class Saida(models.Model):
    descricao = models.ForeignKey(Toner, on_delete=models.CASCADE)
    quantidade_saida = models.IntegerField(default=1)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    data_saida = models.DateField(default=timezone.now())

    def __str__(self):
        return "%s" % (self.departamento.nome)

    def saida_recente(self):
        return self.data_saida >= timezone.now()

    datetime

    class Meta:
        ordering = ['data_saida']










