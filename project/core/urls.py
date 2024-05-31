from django.contrib.auth.views import LogoutView
from django.urls import path

from core.views import index, nosotros, CustomLoginView, register


app_name = "core"


urlpatterns = [
    path("", index, name="index"),
    path("nosotros/", nosotros, name="nosotros"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", register, name="register"),
]
