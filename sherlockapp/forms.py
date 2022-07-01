from django import forms
from .models import SherlockUser

class SherlockForm(forms.ModelForm):

    class Meta:
        model = SherlockUser
        fields = ['username',]