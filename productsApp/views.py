from django.shortcuts import render
from django.http import HttpResponse

from productsApp.models import ProductsApp

# Create your views here.
def create_products(request):
    ProductsApp.objects.create(name="coca cola", price=5000, stock=True)
    return HttpResponse('se creo el nuevo producto')
