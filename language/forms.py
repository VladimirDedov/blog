from django import forms
from .models import *

class AddWordForm(forms.ModelForm):
    class Meta:
        model = Distionary
        fields = [ 'word_eng', 'slug','word_rus',
                   'exemple_1_eng', 'exemple_1_rus',
                   'exemple_2_eng', 'exemple_2_rus',
                   'exemple_3_eng','exemple_3_rus','image'
                   ]
        widgets ={
            'word_eng': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'slug': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'word_rus': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'exemple_1_eng': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'exemple_1_rus': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'exemple_2_eng': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'exemple_2_rus': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'exemple_3_eng': forms.Textarea(attrs={ 'rows': 1, 'class': "form-control"}),
            'exemple_3_rus': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
        }