from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'app_amasanderia/index.html')

def welcome(request):
    return render(request,'app_amasanderia/welcome.html')

def flujos(request):
    return render(request,'app_amasanderia/flujos.html')

def info(request):
    return render(request,'app_amasanderia/info.html')

def formulario(request):
    return render(request,'app_amasanderia/formulario.html')

def resultados(request):
    return render(request,'app_amasanderia/resultados.html',contexto)
