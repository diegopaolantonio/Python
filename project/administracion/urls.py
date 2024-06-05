from django.urls import path

from administracion.views import (
    index,
    FacturaList,
    FacturaCreate,
    FacturaDetail,
    FacturaUpdate,
    FacturaDelete,
    GastoList,
    GastoCreate,
    GastoDetail,
    GastoUpdate,
    GastoDelete,
)


app_name = "administracion"


urlpatterns = [
    path("", index, name="index"),
]

urlpatterns += [
    path("/factura/list", FacturaList.as_view(), name="factura_list"),
    path("/factura/create", FacturaCreate.as_view(), name="factura_create"),
    path("/factura/detail/<int:pk>", FacturaDetail.as_view(), name="factura_detail"),
    path("/factura/update/<int:pk>", FacturaUpdate.as_view(), name="factura_update"),
    path("/factura/delete/<int:pk>", FacturaDelete.as_view(), name="factura_delete"),
]

urlpatterns += [
    path("/gasto/list", GastoList.as_view(), name="gasto_list"),
    path("/gasto/create", GastoCreate.as_view(), name="gasto_create"),
    path("/gasto/detail/<int:pk>", GastoDetail.as_view(), name="gasto_detail"),
    path("/gasto/update/<int:pk>", GastoUpdate.as_view(), name="gasto_update"),
    path("/gasto/delete/<int:pk>", GastoDelete.as_view(), name="gasto_delete"),
]
