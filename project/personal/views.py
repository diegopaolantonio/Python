from django.shortcuts import render, redirect

from personal.models import Area, Personal
from personal.forms import AreaForm, PersonalForm


def index(request):
    return render(request, "personal/index.html")

def area_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Area.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Area.objects.all()
    contexto = {"areas": consulta}
    return render(request, "personal/area_list.html", contexto)

def area_create(request):
    if request.method == "POST":
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("personal:area_list")
    else:
        form = AreaForm()
    return render(request, "personal/area_create.html", {"form": form})

def area_delete(request, pk: int):
    consulta = Area.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("personal:area_list")
    return render(request, "personal/area_delete.html", {"area": consulta})

def area_update(request, pk: int):
    consulta = Area.objects.get(id=pk)
    if request.method == "POST":
        form = AreaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("personal:area_list")
    else:
        form = AreaForm(instance=consulta)
    return render(request, "personal/area_create.html", {"form": form})

def personal_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Personal.objects.filter(Nombre__icontains=busqueda)
    else:
        consulta = Personal.objects.all()
    contexto = {"personal": consulta}
    return render(request, "personal/personal_list.html", contexto)

def personal_create(request):
    if request.method == "POST":
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("personal:personal_list")
    else:
        form = PersonalForm()
    return render(request, "personal/personal_create.html", {"form": form})

def personal_delete(request, pk: int):
    consulta = Personal.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("personal:personal_list")
    return render(request, "personal/personal_delete.html", {"personal": consulta})

def personal_update(request, pk: int):
    consulta = Personal.objects.get(id=pk)
    if request.method == "POST":
        form = PersonalForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("personal:personal_list")
    else:
        form = PersonalForm(instance=consulta)
    return render(request, "personal/personal_create.html", {"form": form})
