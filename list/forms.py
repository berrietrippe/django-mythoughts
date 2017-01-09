from django import forms

from .models import Quote

class addThoughtForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = ('text',)
