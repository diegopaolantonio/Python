from django.urls import path

from personal.views import (
    index,
    AreaList,
    AreaCreate,
    AreaUpdate,
    AreaDelete,
    PersonalList,
    PersonalCreate,
    PersonalDetail,
    PersonalUpdate,
    PersonalDelete,
)


app_name = "personal"

urlpatterns = [
    path("", index, name="index"),
]

urlpatterns += [
    path("/area/list", AreaList.as_view(), name="area_list"),
    path("/area/create", AreaCreate.as_view(), name="area_create"),
    path("/area/update/<int:pk>", AreaUpdate.as_view(), name="area_update"),
    path("/area/delete/<int:pk>", AreaDelete.as_view(), name="area_delete"),
]

urlpatterns += [
    path("/personal/list", PersonalList.as_view(), name="personal_list"),
    path("/personal/create", PersonalCreate.as_view(), name="personal_create"),
    path("/personal/detail/<int:pk>", PersonalDetail.as_view(), name="personal_detail"),
    path("/personal/update/<int:pk>", PersonalUpdate.as_view(), name="personal_update"),
    path("/personal/delete/<int:pk>", PersonalDelete.as_view(), name="personal_delete"),
]
