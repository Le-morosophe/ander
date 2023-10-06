from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)