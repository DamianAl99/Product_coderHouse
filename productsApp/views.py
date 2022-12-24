from django.shortcuts import render
from django.http import HttpResponse

from productsApp.models import ProductsApp, Category

# Create your views here.
def create_products(request):
    ProductsApp.objects.create(name="coca cola", price=5000, stock=True)
    return HttpResponse('se creo el nuevo producto')

def list_products(request):
    all_products = ProductsApp.objects.all()
    context = {
        'products':all_products,
    }
    return render(request, 'products/list_products.html', context=context)

def create_category(request, name):
    Category.objects.create(name=name)
    return HttpResponse('Categoria creada')

def list_categories(request):
    all_categories = Category.objects.all()
    context = {
        'categories':all_categories
    }
    return render(request, 'categories/list_categories.html', context=context)
