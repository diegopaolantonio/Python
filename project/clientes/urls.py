from django.urls import path

from clientes.views import (index, cliente_list, cliente_create, cliente_delete, cliente_update, ubicacion_list, ubicacion_create, ubicacion_delete, ubicacion_update)


app_name = "clientes"


urlpatterns = [
    path("", index, name="index"),
]

urlpatterns += [
    path("/cliente/list", cliente_list.as_view(), name="cliente_list"),
    path("/cliente/create", cliente_create.as_view(), name="cliente_create"),
    path("/cliente/delete/<int:pk>", cliente_delete.as_view(), name="cliente_delete"),
    path("/cliente/update/<int:pk>", cliente_update.as_view(), name="cliente_update"),
]

urlpatterns += [
    path("/ubicacion/list", ubicacion_list.as_view(), name="ubicacion_list"),
    path("/ubicacion/create", ubicacion_create.as_view(), name="ubicacion_create"),
    path("/ubicacion/delete/<int:pk>", ubicacion_delete.as_view(), name="ubicacion_delete"),
    path("/ubicacion/update/<int:pk>", ubicacion_update.as_view(), name="ubicacion_update"),
]