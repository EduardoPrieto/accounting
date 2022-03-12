from django import forms
from .models import Company
from django.forms.widgets import TextInput, Textarea

    
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget = forms.Textarea(attrs={'class': 'form-control'})
        
        

class NewMember(forms.Form):
    user = forms.CharField(widget=TextInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'usuario@ejemplo.com',
        'type': 'email'}))
