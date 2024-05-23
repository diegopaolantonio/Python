from django.urls import path

from clientes.views import index, clientes_list, clientes_create, clientes_delete, clientes_update, ubicacion_list, ubicacion_create, ubicacion_delete, ubicacion_update


app_name = "clientes"


urlpatterns = [
    path("", index, name="index"),
    path("/clientes/list", clientes_list, name="clientes_list"),
    path("/clientes/create", clientes_create, name="clientes_create"),
    path("/clientes/delete/<int:pk>", clientes_delete, name="clientes_delete"),
    path("/clientes/update/<int:pk>", clientes_update, name="clientes_update"),
    path("/ubicacion/list", ubicacion_list, name="ubicacion_list"),
    path("/ubicacion/create", ubicacion_create, name="ubicacion_create"),
    path("/ubicacion/delete/<int:pk>", ubicacion_delete, name="ubicacion_delete"),
    path("/ubicacion/update/<int:pk>", ubicacion_update, name="ubicacion_update"),
]