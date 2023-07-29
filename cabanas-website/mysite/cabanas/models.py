from django.db import models

# Create your models here.
from os import name
from django.db import models
from django.conf import settings
from datetime import datetime, timedelta

class Terms(models.Model):
    time_term = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.time_term}"

class Contact_en(models.Model):
    full_name = models.CharField(max_length=64, name='name')
    email = models.CharField(max_length=64)
    body = models.TextField(name='message')

    def __str__(self):
        return f"{self.id}:{self.full_name}:{self.email}:{self.body}"

class Contact_nl(models.Model):
    full_name = models.CharField(max_length=64, name='naam')
    email = models.CharField(max_length=64, name='e-mail')
    body = models.TextField(name='bericht')

    def __str__(self):
        return f"{self.id}:{self.naam}:{self.email}:{self.bericht}"

class Contact_es(models.Model):
    full_name = models.CharField(max_length=64, name='nombre')
    email = models.CharField(max_length=64, name='correo')
    body = models.TextField(name='mensaje')

    def __str__(self):
        return f"{self.id}:{self.nombre}:{self.correo}:{self.mensaje}"        

class Service(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.CharField(max_length=32)
    img = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.id}:{self.name} - {self.description} (AR${self.price})"

class Sport(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=9)
    img = models.ImageField()
    
    def __str__(self):
        return f"{self.id}:{self.name} - {self.description} (AR${self.price})"

class Gallery(models.Model):
    title = models.CharField(max_length=32)
    img = models.ImageField()

    def __str__(self):
        return f"{self.id} : {self.title}"

class Cabanas_fotos(models.Model):
    title = models.CharField(max_length=32)
    img = models.ImageField()

    def __str__(self):
        return f"{self.id} : {self.title}"

class Subscriptions(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.CharField(max_length=9)
    term = models.ForeignKey(Terms, on_delete=models.CASCADE, default=None)
    img = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.id}:{self.name} - {self.description} (AR${self.price})"

class Cabanas(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField( null=True, blank=True)
    price = models.CharField(max_length=9, null=True, blank=True)
    top_persons_1st_price = models.CharField(max_length=9, null=True, blank=True)
    price_extra_persons = models.CharField(max_length=9, null=True, blank=True)
    top_persons = models.CharField (max_length=9, null=True, blank=True)
    term = models.ForeignKey(Terms, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.id}:{self.name} - AR${self.price} por dia hasta {self.top_persons_1st_price} personas. Por persona adicional AR${self.price_extra_persons} por dia hasta {self.top_persons} personas"

class Text_pag_eventos(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    img1 = models.ImageField(null=True, blank=True)
    img2 = models.ImageField(null=True, blank=True)
    img3 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}:{self.name}"

class Piscina(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    img = models.ImageField(null=True, blank=True)