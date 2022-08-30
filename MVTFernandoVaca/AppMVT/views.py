from django.shortcuts import render
from django.http import HttpResponse

from AppMVT.models import Familia

# Create your views here.

def familia(self):
    familia1=Familia(DNI="343434343",nombre="dsadasda",parentezco="dsadsada",fecha_de_cumpleaños=2022/12/12)
    familia1.save()
    documento=f"DNI: {familia1.DNI} NOMBRE: {familia1.nombre} PARENTEZCO: {familia1.parentezco} FECHA DE CUMPLEAÑOS: {familia1.fecha_de_cumpleaños} "
    return HttpResponse ({"documento":documento})
