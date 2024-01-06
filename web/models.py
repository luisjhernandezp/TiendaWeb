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
