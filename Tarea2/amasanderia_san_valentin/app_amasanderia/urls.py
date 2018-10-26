from django.urls import path
from . import views

urlpatterns = [
	# formato: dirección_pag, función_asociada , name=nombre
    path('',views.index, name='index'),
    path('welcome', views.welcome, name='welcome'),
    path('flujos', views.flujos, name='flujos'),
    path('info', views.info, name='info'),
    path('formulario',        views.formulario,    name='formulario'),
    path('resultados', views.resultados,  name='resultados'),

]