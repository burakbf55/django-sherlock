from django import forms

class SherlockForm(forms.Form):
    username = forms.CharField(max_length = 150)