from django.contrib import admin

# Register your models here.
from .models import Cuenta
from .models import Asiento
from .models import tipocuenta

admin.site.register(Cuenta)
admin.site.register(Asiento)
admin.site.register(tipocuenta)
