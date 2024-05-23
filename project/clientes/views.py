from django.shortcuts import render, redirect

from clientes.models import Cliente, Ubicacion
from clientes.forms import ClientesForm, UbicacionForm


def index(request):
    return render(request, "clientes/index.html")

def clientes_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Cliente.objects.filter(RazonSocial__icontains=busqueda)
    else:
        consulta = Cliente.objects.all()
    contexto = {"clientes": consulta}
    return render(request, "clientes/clientes_list.html", contexto)

def clientes_create(request):
    if request.method == "POST":
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes:clientes_list")
    else:
        form = ClientesForm()
    return render(request, "clientes/clientes_create.html", {"form": form})

def clientes_delete(request, pk: int):
    consulta = Cliente.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("clientes:clientes_list")
    return render(request, "clientes/clientes_delete.html", {"cliente": consulta})

def clientes_update(request, pk: int):
    consulta = Cliente.objects.get(id=pk)
    if request.method == "POST":
        form = ClientesForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("clientes:clientes_list")
    else:
        form = ClientesForm(instance=consulta)
    return render(request, "clientes/clientes_create.html", {"form": form})

def ubicacion_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Ubicacion.objects.filter(pais__icontains=busqueda)
    else:
        consulta = Ubicacion.objects.all()
    contexto = {"ubicaciones": consulta}
    return render(request, "clientes/ubicacion_list.html", contexto)

def ubicacion_create(request):
    if request.method == "POST":
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes:ubicacion_list")
    else:
        form = UbicacionForm()
    return render(request, "clientes/ubicacion_create.html", {"form": form})

def ubicacion_delete(request, pk: int):
    consulta = Ubicacion.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("clientes:ubicacion_list")
    return render(request, "clientes/ubicacion_delete.html", {"ubicacion": consulta})

def ubicacion_update(request, pk: int):
    consulta = Ubicacion.objects.get(id=pk)
    if request.method == "POST":
        form = UbicacionForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("clientes:ubicacion_list")
    else:
        form = UbicacionForm(instance=consulta)
    return render(request, "clientes/ubicacion_create.html", {"form": form})
