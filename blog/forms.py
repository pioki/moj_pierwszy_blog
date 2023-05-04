from django import forms
from .models import Wpis

class WyslijWpis(forms.ModelForm):
  class Meta:
    model = Wpis
    fields = ('tytul','tekst')
