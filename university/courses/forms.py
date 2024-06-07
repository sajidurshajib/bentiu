from django import forms
from .models import Courses
from tinymce.widgets import TinyMCE

class CoursesForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full', 'rows': 5}))
    class Meta:
        model = Courses
        fields = ['name', 'body', 'school']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'
            }),
            'school': forms.Select(attrs={
                'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'
            })
        }