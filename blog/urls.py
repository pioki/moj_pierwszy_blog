from django.urls import path
from . import views

urlpatterns = {
  path('',views.lista_wpisow, name='lista_wpisow'),
}
