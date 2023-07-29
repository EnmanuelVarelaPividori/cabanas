from os import name
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home_es"),
    path('contact/', views.contact, name="contact_es"),
    path('contact/message-sent/', views.successful_message_es, name='succesful-message-es'),
    path('servicios-y-actividades/', views.sya, name="sya_es"),
    path('sobre-nosotros/', views.sobre_nosotros, name="sobre_nosotros_es"),
    path('camping/', views.camping, name="camping"),
    path('subscriptions/', views.subscriptions, name="subscriptions"),
    path('events-and-excursions/', views.events, name="events"),


    path('nl/', views.home_nl, name="home_nl"),
    path('nl/contact/', views.contact_nl, name="contact_nl"),
    path('nl/servicios-y-actividades/', views.sya_nl, name="sya_nl"),
    path('nl/sobre-nosotros/', views.sobre_nosotros_nl, name="sobre_nosotros_nl"),

    path('en/', views.home_en, name="home_en"),
    path('en/contact/', views.contact_en, name="contact_en"),
    path('en/servicios-y-actividades/', views.sya_en, name="sya_en"),
    path('en/sobre-nosotros/', views.sobre_nosotros_en, name="sobre_nosotros_en"),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)