from django.db import models

# Create your models here.
class Eleve(models.Model):
    nomcomplet = models.CharField(max_length=255)
    age = models.IntegerField()
    sexe = models.CharField(max_length=1)
    datenaissance = models.DateField()

    def __str__(self):
        return self.nomcomplet
