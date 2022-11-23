from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def inicio(request):
    return render(request,"AppLOL/index.html")
def items(request):
    return HttpResponse("Los cambios de los items")
def campeones(request):
    return HttpResponse("Buffeos y Nerfeos")