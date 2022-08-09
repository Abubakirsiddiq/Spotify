from django.db import models


class Qoshiqchi(models.Model):
    ism=models.CharField(max_length=100)
    janr=models.CharField(max_length=100)
    mamlakat=models.CharField(max_length=50)
    def __str__(self):
        return self.ism


class Albom(models.Model):
     nom=models.CharField(max_length=120)
     sana=models.DateField()
     qoshiqchi=models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)
     def __str__(self):
        return self.nom


class Qoshiq(models.Model):
     nom=models.CharField(max_length=120)
     eshitish_soni=models.IntegerField(default=0)
     albom=models.ForeignKey(Albom,on_delete=models.CASCADE)
     fayl=models.URLField()
     def __str__(self):
        return self.nom

