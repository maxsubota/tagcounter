from django import forms


class WebsiteForm(forms.Form):
    website = forms.CharField(widget=forms.TextInput(
        attrs= {
            'class': 'form-control',
            'placeholder': 'Input a website'
        }
    ))