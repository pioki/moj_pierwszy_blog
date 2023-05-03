from django.urls import path
from . import views

urlpatterns = [
  path('',views.lista_wpisow, name='lista_wpisow'),
  path('wpis/<int:pk>/',views.szczegoly_wpisu, name='szczegoly_wpisu'),
]
