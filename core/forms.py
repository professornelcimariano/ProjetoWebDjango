from django import forms
from .models import Blog

class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'blo_title': forms.TextInput(attrs={'style': 'width: 80%;'}),
            'blo_subtitle': forms.TextInput(attrs={'style': 'width: 80%;'})            
        }
