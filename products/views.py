from django.shortcuts import render
def vista_contemplate(request):
    context = { 'nombre': 'Jose' }
    return render(request, 'index.html', context=context)

def index(request):
    return render(request, 'index.html', context={})