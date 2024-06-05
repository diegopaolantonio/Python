from django.urls import path

from administracion.views import (index, factura_list, factura_create, factura_delete, factura_update, gasto_list, gasto_create, gasto_delete, gasto_update)


app_name = "administracion"


urlpatterns = [
    path("", index, name="index"),
]

urlpatterns += [
    path("/factura/list", factura_list.as_view(), name="factura_list"),
    path("/factura/create", factura_create.as_view(), name="factura_create"),
    path("/factura/delete/<int:pk>", factura_delete.as_view(), name="factura_delete"),
    path("/factura/update/<int:pk>", factura_update.as_view(), name="factura_update"),
]

urlpatterns += [
    path("/gasto/list", gasto_list.as_view(), name="gasto_list"),
    path("/gasto/create", gasto_create.as_view(), name="gasto_create"),
    path("/gasto/delete/<int:pk>", gasto_delete.as_view(), name="gasto_delete"),
    path("/gasto/update/<int:pk>", gasto_update.as_view(), name="gasto_update"),
]