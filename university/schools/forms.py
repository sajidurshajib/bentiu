from django import forms
from .models import Schools

class SchoolsForm(forms.ModelForm):
    class Meta:
        model = Schools
        fields = ['name', 'body', 'cover', 'position']  # Include the fields you want to show in the form
        widgets = {
            'name': forms.TextInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
            'cover': forms.FileInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full cursor-pointer','accept': 'image/*'}),
            'position': forms.NumberInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
        }