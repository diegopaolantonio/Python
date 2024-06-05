from django.urls import path

from proyectos.views import (
    index,
    ProyectoList,
    ProyectoCreate,
    ProyectoDetail,
    ProyectoUpdate,
    ProyectoDelete,
)


app_name = "proyectos"


urlpatterns = [
    path("", index, name="index"),
]

urlpatterns += [
    path("/proyecto/list", ProyectoList.as_view(), name="proyecto_list"),
    path("/proyecto/create", ProyectoCreate.as_view(), name="proyecto_create"),
    path("/proyecto/detail/<int:pk>", ProyectoDetail.as_view(), name="proyecto_detail"),
    path("/proyecto/update/<int:pk>", ProyectoUpdate.as_view(), name="proyecto_update"),
    path("/proyecto/delete/<int:pk>", ProyectoDelete.as_view(), name="proyecto_delete"),
]
