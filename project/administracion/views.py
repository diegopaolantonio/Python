from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.db.models.query import QuerySet

from administracion.models import Factura, Gasto
from administracion.forms import FacturaForm, GastoForm


def index(request):
    return render(request, "administracion/index.html")

class factura_list(LoginRequiredMixin, ListView):
    model = Factura
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Factura.objects.filter(Numero__icontains=busqueda)
        return queryset

class factura_create(LoginRequiredMixin, CreateView):
    model = Factura
    form_class = FacturaForm
    success_url = reverse_lazy("administracion:factura_list")

class factura_update(LoginRequiredMixin, UpdateView):
    model = Factura
    form_class = FacturaForm
    success_url = reverse_lazy("administracion:factura_list")

class factura_delete(LoginRequiredMixin, DeleteView):
    model = Factura
    success_url = reverse_lazy("administracion:factura_list")

class gasto_list(LoginRequiredMixin, ListView):
    model = Gasto
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Gasto.objects.filter(Referencia__icontains=busqueda)
        return queryset

class gasto_create(LoginRequiredMixin, CreateView):
    model = Gasto
    form_class = GastoForm
    success_url = reverse_lazy("administracion:gasto_list")

class gasto_update(LoginRequiredMixin, UpdateView):
    model = Gasto
    form_class = GastoForm
    success_url = reverse_lazy("administracion:gasto_list")

class gasto_delete(LoginRequiredMixin, DeleteView):
    model = Gasto
    success_url = reverse_lazy("administracion:gasto_list")
