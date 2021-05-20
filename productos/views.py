from django.shortcuts  import render
from django.http        import HttpResponse 
from .models            import  Producto

# Create your views here.

def pagina_principal(request):
    my_prods = Producto.objects.all()
    return render(request,
                'pagina_principal.html',
                {'productos' : my_prods})
##    return HttpResponse('Hola Mundo')

def nuevo(request):
    return HttpResponse('Nuevo producto')