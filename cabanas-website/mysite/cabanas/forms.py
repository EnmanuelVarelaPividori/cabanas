from django import forms
from django.forms import widgets
from .models import Contact_es, Contact_en, Contact_nl

class ContactForm_en(forms.ModelForm):
    class Meta:
        model = Contact_en
        fields = ('name','email','message') 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Full name'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Your message...', 'rows': 3, 'max-rows': 8})
        }

class ContactForm_nl(forms.ModelForm):
    class Meta:
        model = Contact_nl
        fields = ('naam','e-mail','bericht') 
        widgets = {
            'naam': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Naam'}),
            'e-mail': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'E-mail'}),
            'bericht': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Uw bericht...', 'rows': 3, 'max-rows': 8})
        }

class ContactForm_es(forms.ModelForm):
    class Meta:
        model = Contact_es
        fields = ('nombre','correo','mensaje') 
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electronico'}),
            'mensaje': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Mensaje...', 'rows': 2, 'max-rows': 8})
        }
        labels = {
            'nombre':'',
            'correo':'',
            'mensaje':'',

        }

class ContactForm_es_mobile(forms.ModelForm):
    class Meta:
        model = Contact_es
        fields = ('nombre', 'correo', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo', 'size': '50px'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electronico'}),
            'mensaje': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Mensaje...', 'rows': 2, 'max-rows': 8})
        }
        labels = {
            'nombre':'',
            'correo':'',
            'mensaje':'',

        }