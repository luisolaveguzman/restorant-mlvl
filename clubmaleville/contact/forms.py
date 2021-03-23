
from django.forms import ModelForm, EmailInput, TextInput, Textarea

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'mail', 'content']
        widgets = {
            'name': TextInput(attrs={
                'id': 'contact_name',
                'class': 'form-control',
                'name': 'name',
                'data-error': 'Ingrese su nombre',
                'placeholder': 'Nombre',
            }),
            'mail': EmailInput(attrs={
                'id': 'contact_id',
                'class': 'form-control',
                'name': 'email_name',
                'data-error': 'Ingrese su correo',
                'placeholder': 'tu_correo@correo.cl',
            }),
            'content': Textarea (attrs={
                'id': 'message_id',
                'class': 'form-control',
                'name': 'message_name',
                'data-error': 'Intente de nuevo',
                'placeholder': 'Ingrese su mensaje',
            }),
        }

class NewsletterForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['mail']
        widgets = {
            'mail': EmailInput(attrs={
                'id': 'subs-email',
                'class': 'form_input',
                'name': 'EMAIL',
                'data-error': 'Ingrese su correo',
                'placeholder': 'tu_correo@correo.cl',
            }),
        }