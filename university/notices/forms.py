from django import forms
from .models import Notice
from tinymce.widgets import TinyMCE

class NoticeForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full', 'rows': 5}))
    class Meta:
        model = Notice
        fields = ['title', 'body', 'date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
            'date': forms.SelectDateWidget(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
        }



            # 'body': forms.Textarea(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full', 'rows':'5'}),
