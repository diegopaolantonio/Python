from django.urls import path

from proyectos.views import index, proyectos_list, proyectos_create, proyectos_delete, proyectos_update


app_name = "proyectos"


urlpatterns = [
    path("", index, name="index"),
    path("/Proyectos/list", proyectos_list, name="proyectos_list"),
    path("/Proyectos/create", proyectos_create, name="proyectos_create"),
    path("/Proyectos/delete/<int:pk>", proyectos_delete, name="proyectos_delete"),
    path("/Proyectos/update/<int:pk>", proyectos_update, name="proyectos_update"),
]