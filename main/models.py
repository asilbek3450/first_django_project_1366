from django.db import models

# Create your models here.
class Kitob(models.Model):
    nomi = models.CharField(max_length=256)
    muallifi = models.CharField(max_length=256)
    yili = models.DateField(auto_now_add=True)
    betlari_soni = models.IntegerField()
    janri = models.CharField(max_length=256)
    rasmi = models.ImageField(upload_to='rasmlar/')
    malumot = models.TextField()

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"

    def __str__(self):
        return self.nomi
    


class Vazifa(models.Model):
    nomi = models.CharField(max_length=256)
    izoh = models.TextField()

    class Meta:
        verbose_name = "Vazifa"
        verbose_name_plural = "Vazifalar"

    def __str__(self):
        return self.nomi