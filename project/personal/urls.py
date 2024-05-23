from django.urls import path

from personal.views import index, area_list, area_create, area_delete, area_update, personal_list, personal_create, personal_delete, personal_update


app_name = "personal"


urlpatterns = [
    path("", index, name="index"),
    path("/Area/list", area_list, name="area_list"),
    path("/Area/create", area_create, name="area_create"),
    path("/Area/delete/<int:pk>", area_delete, name="area_delete"),
    path("/Area/update/<int:pk>", area_update, name="area_update"),
    path("/personal/list", personal_list, name="personal_list"),
    path("/personal/create", personal_create, name="personal_create"),
    path("/personal/delete/<int:pk>", personal_delete, name="personal_delete"),
    path("/personal/update/<int:pk>", personal_update, name="personal_update"),
]