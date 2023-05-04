from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Wpis
from .forms import WyslijWpis

# Create your views here.

def lista_wpisow(request):
  wpisy = Wpis.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
  return render(request, 'blog/lista_wpisow.html', {'wpisy': wpisy})

def szczegoly_wpisu(request,pk):
  wpis = get_object_or_404(Wpis, pk=pk)
  return render(request, 'blog/szczegoly_wpisu.html', {'wpis': wpis})

def nowy_wpis(request):
  if request.method == "POST":
    formularz = WyslijWpis(request.POST)
    if formularz.is_valid():
      wpis = formularz.save(commit=False)
      wpis.autor = request.user
      wpis.data_opublikowania = timezone.now()
      wpis.save()
      return redirect('szczegoly_wpisu',pk=wpis.pk)
  else:
    formularz = WyslijWpis()
  return render(request, 'blog/edycja_wpisu.html', {'formularz': formularz})

def edycja_wpisu(request,pk):
  wpis = get_object_or_404(Wpis, pk=pk)
  if request.method == "POST":
    formularz = WyslijWpis(request.POST, instance=wpis)
    if formularz.is_valid():
      wpis = formularz.save(commit=False)
      wpis.autor = request.user
      wpis.data_opublikowania = timezone.now()
      wpis.save()
      return redirect('szczegoly_wpisu',pk=wpis.pk)
  else:
    formularz = WyslijWpis(instance = wpis)
  return render(request, 'blog/edycja_wpisu.html', {'formularz': formularz})
