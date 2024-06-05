from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.db.models.query import QuerySet

from proyectos.models import Proyecto
from proyectos.forms import ProyectoForm


def index(request):
    return render(request, "proyectos/index.html")


class ProyectoList(LoginRequiredMixin, ListView):
    model = Proyecto

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Proyecto.objects.filter(Nombre__icontains=busqueda)
        return queryset


class ProyectoCreate(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    success_url = reverse_lazy("proyectos:proyecto_list")


class ProyectoDetail(LoginRequiredMixin, DetailView):
    model = Proyecto


class ProyectoUpdate(LoginRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    success_url = reverse_lazy("proyectos:proyecto_list")


class ProyectoDelete(LoginRequiredMixin, DeleteView):
    model = Proyecto
    success_url = reverse_lazy("proyectos:proyecto_list")
