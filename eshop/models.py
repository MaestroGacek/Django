from django.db import models

# Create your models here.
class Letadlo(models.Model):
    nazev = models.TextField(blank = False, max_length=200)
    cena = models.IntegerField(blank = False)
    popis = models.TextField(blank =True)

    def __str__(self):
        return self.nazev

#class Objednavka (models.Letadlo):
