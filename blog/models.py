from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Wpis(models.Model):
  autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  tytul = models.CharField(max_length=200)
  tekst = models.TextField()
  data_utworzenia = models.DateTimeField(default=timezone.now)
  data_opublikowania = models.DateTimeField(blank=True, null=True)

  def opublikuj(self):
    self.data_opublikowania = timezone.now()
    self.save()

  def __str__(self):
    return self.tytul
