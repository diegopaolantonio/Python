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

from administracion.models import Factura, Gasto
from administracion.forms import FacturaForm, GastoForm


def index(request):
    return render(request, "administracion/index.html")


class FacturaList(LoginRequiredMixin, ListView):
    model = Factura

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Factura.objects.filter(numero__icontains=busqueda)
        return queryset


class FacturaCreate(LoginRequiredMixin, CreateView):
    model = Factura
    form_class = FacturaForm
    success_url = reverse_lazy("administracion:factura_list")


class FacturaDetail(LoginRequiredMixin, DetailView):
    model = Factura


class FacturaUpdate(LoginRequiredMixin, UpdateView):
    model = Factura
    form_class = FacturaForm
    success_url = reverse_lazy("administracion:factura_list")


class FacturaDelete(LoginRequiredMixin, DeleteView):
    model = Factura
    success_url = reverse_lazy("administracion:factura_list")


class GastoList(LoginRequiredMixin, ListView):
    model = Gasto

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Gasto.objects.filter(referencia__icontains=busqueda)
        return queryset


class GastoCreate(LoginRequiredMixin, CreateView):
    model = Gasto
    form_class = GastoForm
    success_url = reverse_lazy("administracion:gasto_list")


class GastoDetail(LoginRequiredMixin, DetailView):
    model = Gasto


class GastoUpdate(LoginRequiredMixin, UpdateView):
    model = Gasto
    form_class = GastoForm
    success_url = reverse_lazy("administracion:gasto_list")


class GastoDelete(LoginRequiredMixin, DeleteView):
    model = Gasto
    success_url = reverse_lazy("administracion:gasto_list")
