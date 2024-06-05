from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.db.models.query import QuerySet

from clientes.models import Cliente, Ubicacion
from clientes.forms import ClienteForm, UbicacionForm


def index(request):
    return render(request, "clientes/index.html")

class cliente_list(LoginRequiredMixin, ListView):
    model = Cliente
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Cliente.objects.filter(RazonSocial__icontains=busqueda)
        return queryset

class cliente_create(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy("clientes:cliente_list")

class cliente_update(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy("clientes:cliente_list")

class cliente_delete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes:cliente_list")

class ubicacion_list(LoginRequiredMixin, ListView):
    model = Ubicacion
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Ubicacion.objects.filter(pais__icontains=busqueda)
        return queryset

class ubicacion_create(LoginRequiredMixin, CreateView):
    model = Ubicacion
    form_class = UbicacionForm
    success_url = reverse_lazy("clientes:ubicacion_list")

class ubicacion_update(LoginRequiredMixin, UpdateView):
    model = Ubicacion
    form_class = UbicacionForm
    success_url = reverse_lazy("clientes:ubicacion_list")

class ubicacion_delete(LoginRequiredMixin, DeleteView):
    model = Ubicacion
    success_url = reverse_lazy("clientes:ubicacion_list")
