from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from .models import Cuenta
from .models import Asiento

from django.db.models import F

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def index(request):
    cuenta = Cuenta.objects.all()
    template = loader.get_template("balances/index.html")
    context = {
        'cuenta': cuenta,
    }
    return HttpResponse(template.render(context))

def asiento(request):
    asiento= list(Asiento.objects.all())
    num=1
    for asiento in asiento:
        print num
        asiento = Asiento.objects.all().get(id=num)
        asiento.ctadebito.saldo = F("saldo") - asiento.total
        asiento.ctacredito.saldo = F("saldo") + asiento.total
        asiento.ctadebito.save(update_fields=["saldo"])
        asiento.ctacredito.save(update_fields=["saldo"])
        num=num+1

    asientos = Asiento.objects.all()
    modelObjects = list(Asiento.objects.all())
    total=0
    for modelObject in modelObjects:
        # Cuenta.objects.filter(descripcion=modelObject.ctadebito).update(saldo=saldo - asiento.total)
        total = total + modelObject.total
    template = loader.get_template("balances/asiento.html")
    context = {
        'asientos': asientos,
        'total': total,
    }
    return HttpResponse(template.render(context))

def comprobacion(request):
    activo = Cuenta.objects.all().filter(tipocuenta='1')
    totalActivo = list( Cuenta.objects.all().filter(tipocuenta='1'))
    totalactivo=0
    for totalActivo in totalActivo:
        totalactivo = totalactivo + totalActivo.saldo

    pasivo = Cuenta.objects.all().exclude(tipocuenta='1')
    totalPasivo = list( Cuenta.objects.all().exclude(tipocuenta='1'))
    totalpasivo=0
    for totalPasivo in totalPasivo:
        totalpasivo = totalpasivo + totalPasivo.saldo
    meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre', 'diciembre']
    template = loader.get_template("balances/comprobacion.html")
    context = {
        'activo': activo,
        'pasivo': pasivo,
        'meses': meses,
        'totalactivo': totalactivo,
        'totalpasivo': totalpasivo
    }
    return HttpResponse(template.render(context))
