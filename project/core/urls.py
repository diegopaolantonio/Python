from django.urls import path

from core.views import index, nosotros


app_name = "core"


urlpatterns = [
    path("", index, name="index"),
    path("/nosotros", nosotros, name="nosotros")
]