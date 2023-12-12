from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=90)
    cedula = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Informe(models.Model):
    fechaAnalisis = models.DateField()
    infoUsuario = models.CharField(max_length=80)
    resultadosAlmacenados = models.CharField(max_length=80)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="prestamoList")
    #medidorDeConsumo = models.ForeignKey(MedidorDeConsumo, on_delete=models.CASCADE)
    def __str__(self):
        return self.__fechaAnalisis

class MedidorDeConsumo(models.Model):
    consumoTotal = models.FloatField()
    def __str__(self):
        return self.consumoTotal

class Registro(models.Model):
    registro = models.CharField(max_length=80)
    def __str__(self):
        return self.registro

class registroDispositivos(models.Model):
    consumoKwh = models.FloatField()
    tiempoDeUso = models.DateField()
    cantidadDispositivos = models.IntegerField()
    def __str__(self):
        return self.consumoKwh

class DISPOSITIVOS(models.Model):
    AIRE_ACONDICIONADO = models.BooleanField()
    ASPIRADORA = models.BooleanField()
    REFRIGERADORA = models.BooleanField()
    TELEVISOR = models.BooleanField()
    DUCHA_ELECTRICA = models.BooleanField()
    def __str__(self):
        return self.AIRE_ACONDICIONADO
