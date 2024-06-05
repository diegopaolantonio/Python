from django.urls import path

from clientes.views import (
    index,
    ClienteList,
    ClienteCreate,
    ClienteDetail,
    ClienteUpdate,
    ClienteDelete,
    UbicacionList,
    UbicacionCreate,
    UbicacionUpdate,
    UbicacionDelete,
)


app_name = "clientes"


urlpatterns = [
    path("", index, name="index"),
]

urlpatterns += [
    path("/cliente/list", ClienteList.as_view(), name="cliente_list"),
    path("/cliente/create", ClienteCreate.as_view(), name="cliente_create"),
    path("/cliente/detail/<int:pk>", ClienteDetail.as_view(), name="cliente_detail"),
    path("/cliente/update/<int:pk>", ClienteUpdate.as_view(), name="cliente_update"),
    path("/cliente/delete/<int:pk>", ClienteDelete.as_view(), name="cliente_delete"),
]

urlpatterns += [
    path("/ubicacion/list", UbicacionList.as_view(), name="ubicacion_list"),
    path("/ubicacion/create", UbicacionCreate.as_view(), name="ubicacion_create"),
    path(
        "/ubicacion/update/<int:pk>", UbicacionUpdate.as_view(), name="ubicacion_update"
    ),
    path(
        "/ubicacion/delete/<int:pk>", UbicacionDelete.as_view(), name="ubicacion_delete"
    ),
]
