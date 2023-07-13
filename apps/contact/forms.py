from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'image', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control valid',
            'placeholder': 'Enter your name',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control valid',
            'placeholder': 'Enter your Email',
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control valid',
            'placeholder': 'Enter Image',
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control valid',
            'placeholder': 'Enter Message',
        })