from django import forms

class RegForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    email=forms.EmailField()
    edad=forms.IntegerField()