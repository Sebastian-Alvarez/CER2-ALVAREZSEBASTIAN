from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('carrito/', views.carrito_vista, name="carrito"),
    path('add/', views.carrito_add, name="carrito_add"),
    path('update/', views.carrito_update, name="carrito_update"),
    path('delete/', views.carrito_delete, name="carrito_delete"),
    path('catalogo/',views.catalogo, name="catalogo")
]
