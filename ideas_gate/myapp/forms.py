from django import forms
from .models import Job
# class PageForm(forms.ModelForm):
#     class Meta:
#         model = Page
#         fields = ['title', 'description']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'image','apply']
    widgets = {
        'apply': forms.URLInput(attrs={'placeholder': 'Enter URL or Email'}),
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['apply'].required = False

        
# class NewPageForm(forms.ModelForm):
#     class Meta:
#         model = NewPage
#         fields = ['title', 'description','apply']
#         widgets = {
#         'apply': forms.URLInput(attrs={'placeholder': 'Enter URL or Email'}),
#     }