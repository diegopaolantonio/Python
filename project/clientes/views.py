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

from clientes.models import Cliente, Ubicacion
from clientes.forms import ClienteForm, UbicacionForm


def index(request):
    return render(request, "clientes/index.html")


class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Cliente.objects.filter(razonSocial__icontains=busqueda)
        return queryset


class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy("clientes:cliente_list")


class ClienteDetail(LoginRequiredMixin, DetailView):
    model = Cliente


class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy("clientes:cliente_list")


class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes:cliente_list")


class UbicacionList(LoginRequiredMixin, ListView):
    model = Ubicacion

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Ubicacion.objects.filter(pais__icontains=busqueda)
        return queryset


class UbicacionCreate(LoginRequiredMixin, CreateView):
    model = Ubicacion
    form_class = UbicacionForm
    success_url = reverse_lazy("clientes:ubicacion_list")


class UbicacionUpdate(LoginRequiredMixin, UpdateView):
    model = Ubicacion
    form_class = UbicacionForm
    success_url = reverse_lazy("clientes:ubicacion_list")


class UbicacionDelete(LoginRequiredMixin, DeleteView):
    model = Ubicacion
    success_url = reverse_lazy("clientes:ubicacion_list")
