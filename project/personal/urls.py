from django.urls import path

from personal.views import (index, area_list, area_create, area_delete, area_update, personal_list, personal_create, personal_delete, personal_update)


app_name = "personal"


urlpatterns = [
    path("", index, name="index"),
]

urlpatterns += [
    path("/Area/list", area_list.as_view(), name="area_list"),
    path("/Area/create", area_create.as_view(), name="area_create"),
    path("/Area/delete/<int:pk>", area_delete.as_view(), name="area_delete"),
    path("/Area/update/<int:pk>", area_update.as_view(), name="area_update"),
]

urlpatterns += [
    path("/personal/list", personal_list.as_view(), name="personal_list"),
    path("/personal/create", personal_create.as_view(), name="personal_create"),
    path("/personal/delete/<int:pk>", personal_delete.as_view(), name="personal_delete"),
    path("/personal/update/<int:pk>", personal_update.as_view(), name="personal_update"),
]
