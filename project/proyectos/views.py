from django.shortcuts import render, redirect

from proyectos.models import Proyecto
from proyectos.forms import ProyectoForm


def index(request):
    return render(request, "proyectos/index.html")

def proyectos_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Proyecto.objects.filter(Nombre__icontains=busqueda)
    else:
        consulta = Proyecto.objects.all()
    contexto = {"proyectos": consulta}
    return render(request, "proyectos/proyectos_list.html", contexto)

def proyectos_create(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("proyectos:proyectos_list")
    else:
        form = ProyectoForm()
    return render(request, "proyectos/proyectos_create.html", {"form": form})

def proyectos_delete(request, pk: int):
    consulta = Proyecto.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("proyectos:proyectos_list")
    return render(request, "proyectos/proyectos_delete.html", {"proyecto": consulta})

def proyectos_update(request, pk: int):
    consulta = Proyecto.objects.get(id=pk)
    if request.method == "POST":
        form = ProyectoForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("proyectos:proyectos_list")
    else:
        form = ProyectoForm(instance=consulta)
    return render(request, "proyectos/proyectos_create.html", {"form": form})
