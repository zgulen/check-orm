from atexit import register
from pyexpat import model
from django.db import models

# Create your models here.
class Team(models.Model):
    COUNTRIES = [ # choices = COUNTRIES
        ('TR', 'Turkey'),
        ('US', 'America'),
        ('DE', 'Germany'),
        ('FR', 'France'),
    ]
    first_name = models.CharField("AD", max_length=30)
    last_name = models.CharField("SOYAD", max_length=30)
    age = models.IntegerField("YAŞ", blank=True, null=True)
    country = models.CharField("ÜLKE", max_length=2, choices=COUNTRIES, default="TR")
    avatar = models.ImageField("Profil fotografı", blank=True, null=True, upload_to='photos/')
    register = models.DateTimeField("Kayıt tarihi", auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} - {self.country}"
    
    class Meta:
        ordering = ['register']