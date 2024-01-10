from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)


    def __str__(self): # Para que me devuelva el nombre de la Categoria
        return self.nombre
    
class Producto(models.Model): # ForeinKey porque es una relacion de 1 a muchos, es decir un celular muchos modelos de celelulares
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT) #RESTRICT es cuando alguien borre una categoria no le permita si ya tiene productos creados, para evitar que haya incrongruencia de datos.
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True) # para que acepte mas de 250 caracteres y null por si no quiere colocar nada. 
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos', blank=True)

    def __str__(self): # Para que me devuelva el nombre del Producto
        return self.nombre
#Esto lo debo colocar arriba, pero se esta haciendo aqui con fines didacticos
from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.RESTRICT)
    cedula = models.CharField(max_length=8)
    sexo = models.CharField(max_length=1, default='M')
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True)
    direccion = models.TextField()

    def __str__(self):
        return self.cedula


class Pedido(models.Model):

    ESTADO_CHOICES =(
        ('0','Solicitado'),
        ('1','Pagado')
    )
    cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    nro_pedido = models.CharField(max_length=20, null=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=1, default='0')

    def __str__(self):
        return self.nro_pedido

class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.RESTRICT)
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cantidad = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.producto.nombre
    


    