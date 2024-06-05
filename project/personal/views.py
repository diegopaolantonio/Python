from typing import Any
from django.contrib.auth.decorators import login_required
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

from personal.models import Area, Personal
from personal.forms import AreaForm, PersonalForm


@login_required
def index(request):
    return render(request, "personal/index.html")


class AreaList(LoginRequiredMixin, ListView):
    model = Area

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Area.objects.filter(nombre__icontains=busqueda)
        return queryset


class AreaCreate(LoginRequiredMixin, CreateView):
    model = Area
    form_class = AreaForm
    success_url = reverse_lazy("personal:area_list")


class AreaUpdate(LoginRequiredMixin, UpdateView):
    model = Area
    form_class = AreaForm
    success_url = reverse_lazy("personal:area_list")


class AreaDelete(LoginRequiredMixin, DeleteView):
    model = Area
    success_url = reverse_lazy("personal:area_list")


class PersonalList(LoginRequiredMixin, ListView):
    model = Personal

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Personal.objects.filter(nombre__icontains=busqueda)
        return queryset


class PersonalCreate(LoginRequiredMixin, CreateView):
    model = Personal
    form_class = PersonalForm
    success_url = reverse_lazy("personal:personal_list")


class PersonalDetail(LoginRequiredMixin, DetailView):
    model = Personal


class PersonalUpdate(LoginRequiredMixin, UpdateView):
    model = Personal
    form_class = PersonalForm
    success_url = reverse_lazy("personal:personal_list")


class PersonalDelete(LoginRequiredMixin, DeleteView):
    model = Personal
    success_url = reverse_lazy("personal:personal_list")
