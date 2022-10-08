from django import forms
from django.forms import ModelForm
from .models import note



class NoteForm(forms.ModelForm):
    class Meta:
        model = note
        fields = ('Title','Description','Date')
        widgets = {
            'Title' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Note Title'}),
            'Description' : forms.Textarea(attrs={'class': 'form-control','placeholder': 'Description'}),
            'Date' : forms.SelectDateWidget(attrs={'class': 'Date-widget'})
        }
        labels ={
            'Title' : '',
            'Description' : '',
            'Date' : ''
        } 