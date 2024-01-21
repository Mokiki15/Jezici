from django.db import models

class Jezik(models.Model):
    Jezik_naziv = models.CharField(max_length=100)

    def __str__(self):
        return self.Jezik_naziv
class Korisnik(models.Model):
    korisnik_ime = models.CharField(max_length=100)
    korisnik_prezime = models.CharField(max_length=100)
    korisnik_jezik = models.ForeignKey(Jezik, default=1, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.korsinik_ime
# Create your models here.
