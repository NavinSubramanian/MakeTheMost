from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    return render(request, 'base/home.html')

def ingridients(request):
    all_item = Items.objects.all()
    context = {'all_item':all_item}
    return render(request, 'base/ingridients.html',context)

def sepitem(request,pk):
    al = Items.objects.get(link=pk)
    waste = Waste.objects.filter(link=al)
    context = {'waste':waste}
    context['link'] = al
    return render(request, 'base/sepitem.html',context)
