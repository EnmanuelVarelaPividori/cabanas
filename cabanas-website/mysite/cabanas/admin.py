from django.contrib import admin

from django.contrib import admin
from .models import  Cabanas, Cabanas_fotos, Contact_es, Gallery, Service, Sport, Subscriptions, Terms, Text_pag_eventos
# Register your models here.
admin.site.register(Service)
admin.site.register(Subscriptions)
admin.site.register(Contact_es)
admin.site.register(Sport)
admin.site.register(Terms)
admin.site.register(Gallery)
admin.site.register(Cabanas)
admin.site.register(Cabanas_fotos)
admin.site.register(Text_pag_eventos)
