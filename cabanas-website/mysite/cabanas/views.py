from django.http.response import BadHeaderError, HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from .forms import ContactForm_es, ContactForm_nl, ContactForm_en
from .models import Cabanas, Cabanas_fotos, Gallery, Service, Sport, Subscriptions, Text_pag_eventos, Piscina
from django.contrib import messages

def send_email_es(correo):
    context = {'correo': correo}
    template = get_template('emails/message-confirmation.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Recibimos tu mensaje! - Cabañas Del Jaaukanigas',
        'Cabañas Del Jaaukanigas',
        settings.EMAIL_HOST_USER,
        [correo]
    )

    email.attach_alternative(content, 'text/html')
    email.send()


## Spanish pages ##

def home(request):
    services = Service.objects.order_by('id')[:4]
    subscriptions = Subscriptions.objects.all()

    form = ContactForm_es()
    if request.method == 'POST':
        correo = request.POST.get('correo')
        send_email_es(correo)
        form = ContactForm_es(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']
            correo = form.cleaned_data['correo']
            send_mail('Cabañasdeljaaukanigas.com - Mensaje de ' + nombre +' ('+ correo +')', mensaje + ' - ' + correo, correo, [settings.EMAIL_HOST_USER])
            return redirect('contact/message-sent/')

    return render(request, 'es/home.html', {
            'form': form,
            'services': services,
            'subscriptions': subscriptions,
        })

def successful_message_es(request):
    form = ContactForm_es()
    if request.method == 'POST':
        correo = request.POST.get('correo')
        send_email_es(correo)
        form = ContactForm_es(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']
            correo = form.cleaned_data['correo']
            send_mail('Cabañasdeljaaukanigas.com - Mensaje de ' + nombre +' ('+ correo +')', mensaje + ' - ' + correo, correo, [settings.EMAIL_HOST_USER])

    return render(request, 'es/message-sent.html', {
            'form': form
        })

def contact(request):
    form = ContactForm_es()
    if request.method == 'POST':
        correo = request.POST.get('correo')
        send_email_es(correo)
        form = ContactForm_es(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']
            correo = form.cleaned_data['correo']
            send_mail('Cabañasdeljaaukanigas.com - Mensaje de ' + nombre +' ('+ correo +')', mensaje + ' - ' + correo, correo, [settings.EMAIL_HOST_USER])
            return redirect('message-sent/')

    return render(request, 'es/contact.html',{
            'form': form,
        })

def sya(request):
    services = Service.objects.all()
    piscinas = Piscina.objects.all()
    sports = Sport.objects.all()
    cabanas_fotos = Cabanas_fotos.objects.all()
    cabanas = Cabanas.objects.all()

    form = ContactForm_es()
    if request.method == 'POST':
        correo = request.POST.get('correo')
        send_email_es(correo)
        form = ContactForm_es(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']
            correo = form.cleaned_data['correo']
            send_mail('Cabañasdeljaaukanigas.com - Mensaje de ' + nombre +' ('+ correo +')', mensaje + ' - ' + correo, correo, [settings.EMAIL_HOST_USER])
            return redirect('../contact/message-sent/')

    return render(request, 'es/sya.html' ,{
        'services': services,
        'sports': sports,
        'form': form,
        'cabanas': cabanas,
        'piscinas': piscinas,
        'cabanas_fotos': cabanas_fotos
    })

def service(request, service_id):
    service = Service.objects.get(pk=service_id)
    return render(request, "admin/service.html", {
        "service": service
    })

def sobre_nosotros(request):
    form = ContactForm_es()
    if request.method == 'POST':
        correo = request.POST.get('correo')
        send_email_es(correo)
        form = ContactForm_es(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']
            correo = form.cleaned_data['correo']
            send_mail('Cabañasdeljaaukanigas.com - Mensaje de ' + nombre +' ('+ correo +')', mensaje + ' - ' + correo, correo, [settings.EMAIL_HOST_USER])
            return redirect('../contact/message-sent/')

    return render(request, 'es/sobre_nosotros.html',{
            'form': form,
        })


def subscriptions(request):
    form = ContactForm_es()
    if request.method == 'POST':
        correo = request.POST.get('correo')
        send_email_es(correo)
        form = ContactForm_es(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']
            correo = form.cleaned_data['correo']
            send_mail('Cabañasdeljaaukanigas.com - Mensaje de ' + nombre +' ('+ correo +')', mensaje + ' - ' + correo, correo, [settings.EMAIL_HOST_USER])
            return redirect('../contact/message-sent/')

    return render (request, 'es/subscriptions.html',{
            'form': form,
        })

def camping(request):
    form = ContactForm_es()
    if request.method == 'POST':
        correo = request.POST.get('correo')
        send_email_es(correo)
        form = ContactForm_es(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']
            correo = form.cleaned_data['correo']
            send_mail('Cabañasdeljaaukanigas.com - Mensaje de ' + nombre +' ('+ correo +')', mensaje + ' - ' + correo, correo, [settings.EMAIL_HOST_USER])
            return redirect('../contact/message-sent/')

    return render (request, 'es/camping.html',{
            'form': form,
        })

def events(request):
    text_pag_eventoss = Text_pag_eventos.objects.all()
    form = ContactForm_es()
    if request.method == 'POST':
        correo = request.POST.get('correo')
        send_email_es(correo)
        form = ContactForm_es(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']
            correo = form.cleaned_data['correo']
            send_mail('Cabañasdeljaaukanigas.com - Mensaje de ' + nombre +' ('+ correo +')', mensaje + ' - ' + correo, correo, [settings.EMAIL_HOST_USER])
            return redirect('../contact/message-sent/')
            
    return render (request, 'es/events.html',{
            'form': form,
            'text_pag_eventoss': text_pag_eventoss
        })



## English pages ##
def home_en(request):
    services = Service.objects.order_by('id')[:6]
    form = ContactForm_en()
    if request.method == 'POST':
        email = request.POST.get('email')
        send_email(email)
        form = ContactForm_en(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Correo electronico']
            full_name = form.cleaned_data['Nombre']
            body = form.cleaned_data['Mensaje']
    return render(request, 'en/home.html', {
            'form': form,
            'services': services,
        })

def contact_en(request):
    form = ContactForm_en()
    if request.method == 'POST':
        email = request.POST.get('email')
        send_email(email)
        form = ContactForm_en(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Correo electronico']
            full_name = form.cleaned_data['Nombre']
            body = form.cleaned_data['Mensaje']
    return render(request, 'en/contact.html', {
            'form': form,
        })

def sya_en(request):
    services = Service.objects.all()
    sports = Sport.objects.all()
    return render(request, 'en/sya.html' ,{
        'services': services,
        'sports': sports,
    })

def sobre_nosotros_en(request):
    return render(request, 'en/sobre_nosotros.html')

## Dutch pages ##

def home_nl(request):
    services = Service.objects.order_by('id')[:6]
    form = ContactForm_nl()
    if request.method == 'POST':
        email = request.POST.get('email')
        send_email(email)
        form = ContactForm_nl(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Correo electronico']
            full_name = form.cleaned_data['Nombre']
            body = form.cleaned_data['Mensaje']
    return render(request, 'nl/home.html', {
            'form': form,
            'services': services,
        })

def contact_nl(request):
    form = ContactForm_nl()
    if request.method == 'POST':
        email = request.POST.get('email')
        send_email(email)
        form = ContactForm_nl(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Correo electronico']
            full_name = form.cleaned_data['Nombre']
            body = form.cleaned_data['Mensaje']
    return render(request, 'nl/contact.html', {
            'form': form,
        })

def sya_nl(request):
    services = Service.objects.all()
    sports = Sport.objects.all()
    return render(request, 'nl/sya.html' ,{
        'services': services,
        'sports': sports,
    })

def sobre_nosotros_nl(request):
    return render(request, 'nl/sobre_nosotros.html')