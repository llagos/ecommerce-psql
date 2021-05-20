from django.contrib import admin
from .models        import  Producto, Oferta

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','moneda' ,'precio', 'existencia', 'descripcion','imagen_url')

class OfertaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'descuento')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Oferta, OfertaAdmin)