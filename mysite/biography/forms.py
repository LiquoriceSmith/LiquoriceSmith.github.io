from django import forms
from .models import Otzivy


class OtzivForm(forms.ModelForm):
    class Meta:
        model = Otzivy
        fields = ['name', 'otziv']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'otziv': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

        }

    def clean_title(self):
        name = self.cleaned_data['name']
        return name
