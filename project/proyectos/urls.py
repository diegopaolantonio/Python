from django.urls import path

from proyectos.views import (index, proyecto_list, proyecto_create, proyecto_delete, proyecto_update)


app_name = "proyectos"


urlpatterns = [
    path("", index, name="index"),
]

urlpatterns += [
    path("/Proyecto/list", proyecto_list.as_view(), name="proyecto_list"),
    path("/Proyecto/create", proyecto_create.as_view(), name="proyecto_create"),
    path("/Proyecto/delete/<int:pk>", proyecto_delete.as_view(), name="proyecto_delete"),
    path("/Proyecto/update/<int:pk>", proyecto_update.as_view(), name="proyecto_update"),
]