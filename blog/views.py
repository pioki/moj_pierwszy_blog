from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Wpis

# Create your views here.

def lista_wpisow(request):
  wpisy = Wpis.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
  return render(request, 'blog/lista_wpisow.html', {'wpisy': wpisy})

def szczegoly_wpisu(request,pk):
  wpis = get_object_or_404(Wpis, pk=pk)
  return render(request, 'blog/szczegoly_wpisu.html', {'wpis': wpis})
