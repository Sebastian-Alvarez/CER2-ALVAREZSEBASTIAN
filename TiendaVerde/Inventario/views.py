from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .carrito import Carrito
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo.html',{'productos':productos})

#CRUD -> Create , Read , Update , Delete

# Create 
def carrito_add(request):
    carrito = Carrito(request)
    if request.POST.get('action') == 'post':
        id_producto = int(request.POST.get('product_id'))
        producto = get_object_or_404(Producto, id=id_producto)
        carrito.add(producto)
        response = JsonResponse({'Nombre Producto:':producto.name})
        return response

# Read
def carrito_vista(request):
    return render(request, 'carrito.html')

# Update
def carrito_update(request):
    pass

# Delete
def carrito_delete(request):
    pass