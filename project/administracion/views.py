from django.shortcuts import render, redirect

from administracion.models import Factura, Gasto
from administracion.forms import FacturasForm, GastosForm


def index(request):
    return render(request, "administracion/index.html")

def facturas_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Factura.objects.filter(Cliente__icontains=busqueda)
    else:
        consulta = Factura.objects.all()
    contexto = {"facturas": consulta}
    return render(request, "administracion/facturas_list.html", contexto)

def facturas_create(request):
    if request.method == "POST":
        form = FacturasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("administracion:facturas_list")
    else:
        form = FacturasForm()
    return render(request, "administracion/facturas_create.html", {"form": form})

def facturas_delete(request, pk: int):
    consulta = Factura.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("administracion:facturas_list")
    return render(request, "administracion/facturas_delete.html", {"factura": consulta})

def facturas_update(request, pk: int):
    consulta = Factura.objects.get(id=pk)
    if request.method == "POST":
        form = FacturasForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("administracion:facturas_list")
    else:
        form = FacturasForm(instance=consulta)
    return render(request, "administracion/facturas_create.html", {"form": form})

def gastos_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Gasto.objects.filter(Referencia__icontains=busqueda)
    else:
        consulta = Gasto.objects.all()
    contexto = {"gastos": consulta}
    return render(request, "administracion/gastos_list.html", contexto)

def gastos_create(request):
    if request.method == "POST":
        form = GastosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("administracion:gastos_list")
    else:
        form = GastosForm()
    return render(request, "administracion/gastos_create.html", {"form": form})

def gastos_delete(request, pk: int):
    consulta = Gasto.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("administracion:gastos_list")
    return render(request, "administracion/gastos_delete.html", {"gasto": consulta})

def gastos_update(request, pk: int):
    consulta = Gasto.objects.get(id=pk)
    if request.method == "POST":
        form = GastosForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("administracion:gastos_list")
    else:
        form = GastosForm(instance=consulta)
    return render(request, "administracion/gastos_create.html", {"form": form})
