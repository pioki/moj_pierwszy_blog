from django.urls import path
from . import views

urlpatterns = [
  path('',views.lista_wpisow, name='lista_wpisow'),
  path('wpis/<int:pk>/',views.szczegoly_wpisu, name='szczegoly_wpisu'),
  path('wpis/nowy',views.nowy_wpis, name='nowy_wpis'),
  path('wpis/<int:pk>/edycja',views.edycja_wpisu, name='edycja_wpisu'),
]
