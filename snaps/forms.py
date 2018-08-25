from django import forms
from .models import Snap, Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name']
        widgets = {
            'first_name' : forms.TextInput(attrs = {'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs = {'class': 'form-control'}),
            'email' : forms.TextInput(attrs = {'class': 'form-control'}),
        }

class SnapForm(forms.ModelForm):
    class Meta:
        model = Snap
        fields = ['image', 'name', 'pub_date', 'caption', 'album']
        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control', 'style':"width: 70%;"}),
            'pub_date': forms.TextInput(attrs = {'class': 'form-control', 'style':"width: 70%;"}),
            'caption': forms.TextInput(attrs = {'class': 'form-control', 'style':"width: 70%;"}),
            'album': forms.TextInput(attrs = {'class': 'form-control', 'style':"width: 70%;", 'placeholder': "General Upload"}),
        }

