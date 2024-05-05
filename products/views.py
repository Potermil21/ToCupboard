from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .models import UserRegistrationForm

# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponse('Welcome to PyShop New Arrivals')

def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Procesar el formulario
            pass  # Aquí deberías agregar el código para procesar el formulario
    else:
        form = UserRegistrationForm()
    return render(request, 'registro.html', {'form': form})