from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.db.models.query import QuerySet

from personal.models import Area, Personal
from personal.forms import AreaForm, PersonalForm


def index(request):
    return render(request, "personal/index.html")

class area_list(LoginRequiredMixin, ListView):
    model = Area
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Area.objects.filter(nombre__icontains=busqueda)
        return queryset

class area_create(LoginRequiredMixin, CreateView):
    model = Area
    form_class = AreaForm
    success_url = reverse_lazy("personal:area_list")

class area_update(LoginRequiredMixin, UpdateView):
    model = Area
    form_class = AreaForm
    success_url = reverse_lazy("personal:area_list")

class area_delete(LoginRequiredMixin, DeleteView):
    model = Area
    success_url = reverse_lazy("personal:area_list")

class personal_list(LoginRequiredMixin, ListView):
    model = Personal
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Personal.objects.filter(Nombre__icontains=busqueda)
        return queryset

class personal_create(LoginRequiredMixin, CreateView):
    model = Personal
    form_class = PersonalForm
    success_url = reverse_lazy("personal:personal_list")

class personal_update(LoginRequiredMixin, UpdateView):
    model = Personal
    form_class = PersonalForm
    success_url = reverse_lazy("personal:personal_list")

class personal_delete(LoginRequiredMixin, DeleteView):
    model = Personal
    success_url = reverse_lazy("personal:personal_list")
