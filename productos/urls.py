from django.urls    import path
from .              import views
## import views ... esto es riesgoso pq puede haber otro módulo "views"

urlpatterns = [
    path('', views.pagina_principal),  ## sin argumentos... es una referencia.. django completa después
    path('new',views.nuevo)
]