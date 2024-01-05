from django.contrib import admin
from .models import Categoria,Producto

# Register your models here.
admin.site.register(Categoria)
# admin.site.register(Producto)

@admin.register(Producto) # Este decorador hace lo mismo que esto: admin.site.register(Producto), pero debajo creo la clase para poder ver
# los camos adicionales en el panel de administracion.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'fecha_registro',) # Esto debe ser una tupla
    list_editable = ('precio',) # para que el precio de los productos desde el panel de administracion se pueda editar
