from django import forms
from .models import Personne

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Personne()
        fields = ['name', 'image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }
