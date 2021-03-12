from django.forms import ModelForm, EmailInput, DateInput, TimeInput, NumberInput, TextInput

from .models import Reservation


class CreateReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'mail', 'phone', 'date', 'hour', 'cant', 'detail']
        widgets = {
            'date':DateInput(attrs={
                'id':'input_date',
                'type':'date',
                'class':'form-control',
                'aria-owns':'input_date_root',
                'placeholder':'Fecha de reservación',
            }),
            'hour': TimeInput(attrs={
                'id': 'input_time',
                'class': 'time form-control picker__input',
                'name': 'hour',
                'type':'time',
                'data-error': 'Ingrese una hora',
                'placeholder': 'Hora de reservación',
            }),
            'cant': NumberInput(attrs={
                'id': 'person',
                'class': 'd-block form-control',
                'name': 'cant',
                'data-error': 'Ingrese la cantidad de personas de la reserva',
                'placeholder': 'Personas',
            }),
            'name': TextInput(attrs={
                'id': 'name',
                'class': 'form-control',
                'name': 'name',
                'data-error': 'Ingrese su nombre',
                'placeholder': 'Nombre',
            }),
            'mail': EmailInput(attrs={
                'id': 'id_email',
                'class': 'form-control',
                'name': 'id_email',
                'data-error': 'Ingrese su correo',
                'placeholder': 'tu_correo@correo.cl',
            }),
            'phone': NumberInput(attrs={
                'id': 'phone',
                'class': 'form-control',
                'name': 'phone',
                'data-error': 'Ingrese su teléfono',
                'placeholder': 'Teléfono ejemplo: 91234567',
            }),
            'detail': TextInput(attrs={
                'id': 'detail',
                'class': 'form-control',
                'name': 'detail',
                'data-error': 'Intente de nuevo',
                'placeholder': 'Puede ingresar detalles acerca de su reserva',
            }),
        }