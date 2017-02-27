from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from .models import Cuenta
from .models import Asiento
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def index(request):
    cuenta = Cuenta.objects.all()
    template = loader.get_template("balances/index.html")
    #contexto = Context({'cuenta':cuenta})
    context = {
        'cuenta': cuenta,

    }
    return HttpResponse(template.render(context))

def asiento(request):
    asiento = Asiento.objects.all()
    modelObjects = list(Asiento.objects.all())
    total=0
    for modelObject in modelObjects:
        total = total + modelObject.total
    print total
    template = loader.get_template("balances/asiento.html")
    context = {
        'asiento': asiento,
        'total': total,
    }
    return HttpResponse(template.render(context))
