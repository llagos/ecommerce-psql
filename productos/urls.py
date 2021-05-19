from django.urls    import path
from .              import views ## import views ... puede haber otro módulo "views"

urlpatterns = [
    path('', index_page)  ## sin argumentos... es una referencia.. django completa después
]