from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context, loader
from AppMVT.models import *
from Plantillas import *

# Create your views here.

def familia(request):
    familiar1=Familia(DNI=37497802,nombre="Fernando",parentezco="Hijo")#,fecha_de_cumpleaños=1993/10/14)
    familiar2=Familia(DNI=14567687,nombre="Virginia",parentezco="Madre")#,fecha_de_cumpleaños=1963/12/4)
    familiar3=Familia(DNI=39456987,nombre="Agustina",parentezco="Hija")#,fecha_de_cumpleaños=1995/9/25)
    familiar1.save()
    familiar2.save()
    familiar3.save()
    texto=f"Hola"
    return HttpResponse(texto)


def Template(request):
    familia1=Familia(id=1,DNI=37497802,nombre="Fernando",parentezco="Hijo")#,fecha_de_cumpleaños=1993/10/14)
    familia2=Familia(id=2,DNI=14567687,nombre="Virginia",parentezco="Madre")#,fecha_de_cumpleaños=1963/12/4)
    familia3=Familia(id=3,DNI=39456987,nombre="Agustina",parentezco="Hija")#,fecha_de_cumpleaños=1995/9/25)
    diccionario={"Familiar1":familia1,"Familiar2":familia2,"Familiar3":familia3}
    plantilla=loader.get_template("Template.html")
    Documento=plantilla.render(diccionario)
    return HttpResponse(Documento)
