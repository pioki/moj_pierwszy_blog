from django.shortcuts import render

# Create your views here.

def lista_wpisow(request):
  return render(request, 'blog/lista_wpisow.html', {})
