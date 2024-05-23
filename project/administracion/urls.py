from django.urls import path

from administracion.views import index, facturas_list, facturas_create, facturas_delete, facturas_update, gastos_list, gastos_create, gastos_delete, gastos_update


app_name = "administracion"


urlpatterns = [
    path("", index, name="index"),
    path("/facturas/list", facturas_list, name="facturas_list"),
    path("/facturas/create", facturas_create, name="facturas_create"),
    path("/facturas/delete/<int:pk>", facturas_delete, name="facturas_delete"),
    path("/facturas/update/<int:pk>", facturas_update, name="facturas_update"),
    path("/gastos/list", gastos_list, name="gastos_list"),
    path("/gastos/create", gastos_create, name="gastos_create"),
    path("/gastos/delete/<int:pk>", gastos_delete, name="gastos_delete"),
    path("/gastos/update/<int:pk>", gastos_update, name="gastos_update"),
]