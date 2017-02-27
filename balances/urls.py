from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cuentas/$', views.index, name='index'),
    url(r'^asiento/$', views.asiento, name='asiento'),
]
