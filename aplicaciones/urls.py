from django.urls import path
from .views import (
    HomeView, CarritoView, AgregarLibroView, EliminarLibroView, LibrosPorGeneroView,
    RestarLibroView, LimpiarCarritoView, RegistroView, LoginView, LibroDetailView,
    CompraExitosaView,CompraRechazadaView,CheckOutView
)

urlpatterns = [
    #URL HOME
    path('', HomeView.as_view(), name='home'),
    #URLS CARRITO
    path('carrito/', CarritoView.as_view(), name='carrito'),
    path('agregar/<str:isbn>/', AgregarLibroView.as_view(), name='agregar_libro'),
    path('eliminar/<str:isbn>/', EliminarLibroView.as_view(), name='eliminar_libro'),
    path('restar/<str:isbn>/', RestarLibroView.as_view(), name='restar_libro'),
    path('limpiar/', LimpiarCarritoView.as_view(), name='limpiar_carrito'),
    path('compra-exitosa/', CompraExitosaView.as_view(), name='compra_exitosa'),
    path('compra-rechazada/', CompraRechazadaView.as_view(), name='compra_rechazada'),
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    #URL CATEGORIA
    path('libros/<str:genero>/', LibrosPorGeneroView.as_view(), name='libros_por_genero'),
    #URL ITEM
    path('libro/<str:isbn>/', LibroDetailView.as_view(), name='libro_detallado'),
    #URLS LOGEO
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
]


