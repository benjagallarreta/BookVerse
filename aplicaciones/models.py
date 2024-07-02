from django.db import models
from django.contrib.auth.models import AbstractUser

#SE EXTIENDE DE USUARIO QUE VIENE POR DEFECTO DE DJANGO
class Usuario(AbstractUser):
    domicilio = models.CharField(max_length=250, null=True, blank=True)
    nacionalidad = models.CharField(max_length=80, null=True, blank=True)
    nroTelefono = models.CharField(max_length=80, null=True, blank=True)
    correoElectronicoSecundario = models.CharField(max_length=250, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def _str_(self):
        return self.username

class TipoLibro (models.TextChoices):
    FISICO = 'F', 'Fisico'
    AUDIO = 'A', 'Audio'
    ELECTRONICO = 'E', 'Electronico'
    
class Libro(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    titulo = models.CharField(max_length=100, blank=False)
    sinopsis = models.TextField(blank=False, default='Sinopsis no disponible')
    autor = models.CharField(max_length=100, blank=False)
    editorial = models.CharField(max_length=100, blank=False)
    genero = models.CharField(max_length=100, blank=False)
    tipo = models.CharField(max_length=1, choices=TipoLibro.choices, default=TipoLibro.FISICO)
    paginas = models.PositiveSmallIntegerField(null=True, blank=True)
    dimension = models.CharField(max_length=50, null=True, blank=True)
    encuadernacion = models.CharField(max_length=50, null=True, blank=True)
    narrador = models.CharField(max_length=100, null=True, blank=True)
    duracion = models.SmallIntegerField(null=True, blank=True)
    extension_archivo = models.CharField(max_length=10, null=True, blank=True)
    portada = models.ImageField(blank=True, upload_to='static/portada', null=True, verbose_name='Imagen del libro')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=False, blank=False)

    def _str_(self):
        return self.isbn

class Reseña(models.Model):
    fecha = models.DateField()
    estrellas = models.CharField(max_length=5)
    comentario = models.TextField(max_length=500)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, default=None)

class BilleteraVirtual(models.Model):
    monto = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)

class Estado(models.TextChoices):
    PENDIENTE = 'P', 'Pendiente'
    EN_PROCESO = 'E', 'En proceso'
    ENVIADO = 'N', 'Enviado'
    ENTREGADO = 'D', 'Entregado'
    CANCELADO = 'C', 'Cancelado'

class Pedido(models.Model):
    monto = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)
    origen = models.CharField(max_length=20)
    estado = models.CharField(max_length=1, choices=Estado.choices)