from django import forms
from .models import *

class content_manager(forms.ModelForm):
    comments = forms.CharField(widget = forms.Textarea,label = '内容',required = True)