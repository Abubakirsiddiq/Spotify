from django.db import models


class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=30)
    janr = models.CharField(max_length=30)
    mamlakat = models.CharField(max_length=30)
    def __str__(self):
        return self.ism


class Albom(models.Model):
    nom = models.CharField(max_length=50)
    sana = models.DateField()
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom


class Qoshiq(models.Model):
    nom = models.CharField(max_length=50)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)
    fayl = models.URLField()
    eshitish_soni = models.IntegerField(default=0)
    def __str__(self):
        return self.nom

