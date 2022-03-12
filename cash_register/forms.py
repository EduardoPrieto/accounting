
from django import forms
from .models import Expenses, Sales
from django.forms.widgets import ClearableFileInput, DateInput
from django.forms.widgets import TextInput, DateInput, FileInput
from datetime import datetime

excpenses_type = [('', '...'), ('Nómina', 'Nómina'), ('Proveedores', 'Proveedores'), ('Pagos a accionistas', 'Pagos a accionistas'), ('Varios', 'Varios')]
payments_type = [('', '...'), ('Efectivo', 'Efectivo'), ('Consignación', 'Consignación')]

# Tipo de gasto - efectivo / consignación

#Form para contrato, se añaden algunas validaciones aparte de las de fronEnd
#Se aplican las clases que llevaran los estilos
class ExpensesForm(forms.ModelForm):
    expense_type = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=excpenses_type, label="Tipo de gasto")
    payment_type = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=payments_type, label="Tipo de pago")
    class Meta:
        model = Expenses
        fields = '__all__'
        widgets = {
            'name': forms.DateInput(attrs={'class': 'form-control', 'type': 'text'}),
            'date': forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'datepicker form-control', 'type': 'date'}),
        }

class SalesForm(forms.ModelForm):
    payment_type = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=payments_type, label="Tipo de pago")
    class Meta:
        model = Sales
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'datepicker form-control', 'type': 'date'}),
        }