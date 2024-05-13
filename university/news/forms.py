from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'body', 'cover', 'date']  # Include the fields you want to show in the form
        widgets = {
            'title': forms.TextInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
            'cover': forms.FileInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full cursor-pointer','accept': 'image/*'}),
            'date': forms.SelectDateWidget(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
        }