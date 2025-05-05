from django import forms

class QRCodeForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        label="Title ",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a name or title for this QR code'

        })
        )
    
    url = forms.URLField(
        max_length=200,
        label='URL ',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the URL you want to encode'
        })
        )
