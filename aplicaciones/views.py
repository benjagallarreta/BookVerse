from decimal import Decimal
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, View, DetailView
from .forms import RegistroForm, LoginForm
from .models import Libro
from aplicaciones.Carrito import Carrito
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#VIEW HOME
class HomeView(ListView):
    model = Libro
    template_name = 'home.html'
    context_object_name = 'libros'
    paginate_by = 20

    #Agarra todos los forms del html de tipo get
    def get_queryset(self):
        queryset = Libro.objects.all()
        search_query = self.request.GET.get('buscar')

        if search_query:
            queryset = queryset.filter(
                Q(titulo__icontains=search_query) |
                Q(autor__icontains=search_query) |
                Q(isbn__icontains=search_query)
            )

        return queryset

#VIEWS CARRITO
class CarritoView(ListView):
    model = Libro
    template_name = 'Carrito.html'
    context_object_name = 'libros'

class AgregarLibroView(View):
    def get(self, request, isbn):
        carrito = Carrito(request)
        libro = Libro.objects.get(isbn=isbn)
        carrito.agregar(libro)
        referer = request.META.get('HTTP_REFERER', 'home')
        return HttpResponseRedirect(referer)

    def post(self, request, isbn):
        carrito = Carrito(request)
        libro = Libro.objects.get(isbn=isbn)
        carrito.agregar(libro)
        referer = request.META.get('HTTP_REFERER', 'home')
        return HttpResponseRedirect(referer)

class EliminarLibroView(View):
    def get(self, request, isbn):
        carrito = Carrito(request)
        libro = Libro.objects.get(isbn=isbn)
        carrito.eliminar(libro)
        return redirect('carrito')

class RestarLibroView(View):
    def get(self, request, isbn):
        carrito = Carrito(request)
        libro = Libro.objects.get(isbn=isbn)
        carrito.restar(libro)
        return redirect('carrito')

class LimpiarCarritoView(View):
    def get(self, request):
        carrito = Carrito(request)
        carrito.limpiar()
        return redirect('carrito')

@method_decorator(login_required, name='dispatch')
class CompraExitosaView(View):
    template_name = 'CompraRealizada.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

@method_decorator(login_required, name='dispatch')  
class CompraRechazadaView(View):
    template_name = 'errorCompra.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

@method_decorator(login_required, name='dispatch')
class CheckOutView(View):

    def get(self, request, *args, **kwargs):

        total = Decimal('0.00')
        if request.session.get("carrito"):
            for key, value in request.session["carrito"].items():
                total += Decimal(value.get("Acumulado", '0.00'))

        total_float = float(total)

        if total == Decimal('0.00'):
            return redirect('/')

        #Si se pasa de los 100.000 no puede realizar compra sino si puede
        if total_float > 100000:
            return redirect('compra_rechazada')
        else:
            if 'carrito' in request.session:
                del request.session['carrito']
            return redirect('compra_exitosa')

#VIEW CATEGORIA
class LibrosPorGeneroView(View):
    def get(self, request, genero):
        libros = Libro.objects.filter(genero__icontains=genero)
        context = {
            'libros': libros,
            'genero': genero
        }
        return render(request, 'libros_por_genero.html', context)

#VIEW ITEM  
class LibroDetailView(DetailView):
    model = Libro
    template_name = 'Item.html'
    context_object_name = 'libro'

    def get_object(self):
        isbn = self.kwargs.get("isbn")
        return get_object_or_404(Libro, isbn=isbn)
        
#VIEWS LOGEO
class RegistroView(View):
    def get(self, request):
        form = RegistroForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        return render(request, 'registration/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, "Nombre de usuario o contraseña incorrectos")
        return render(request, 'registration/login.html', {'form': form})
