from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import AuthenticationForm#Встроенный  класс авторизации
from django.contrib.auth.models import User



class AddWordForm(forms.ModelForm):
    """form of added word"""
    class Meta:
        model = Distionary
        fields = ['word_eng', 'slug', 'word_rus',
                  'exemple_1_eng', 'exemple_1_rus',
                  'exemple_2_eng', 'exemple_2_rus',
                  'exemple_3_eng', 'exemple_3_rus', 'image'
                  ]
        widgets = {
            'word_eng': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'slug': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'word_rus': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'exemple_1_eng': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'exemple_1_rus': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'exemple_2_eng': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'exemple_2_rus': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'exemple_3_eng': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'exemple_3_rus': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
        }


class AddPostForm(forms.ModelForm):
    """form of added post """
    #date_add = forms.DateField(label="Дата создания", widget=forms.SelectDateWidget)
    field_order = ['title','slug', 'content','date_add', 'category', 'image_1', 'image_2', 'image_3']
    content = forms.CharField(widget=CKEditorWidget(attrs={'class': "form-control"}), label='Содержание' )
    class Meta:
        model = Blog
        fields = { 'title', 'slug', 'content', 'date_add','image_3', 'category', 'image_1', 'image_2'}
        widgets = {
            'title': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'slug': forms.Textarea(attrs={'rows': 1, 'class': "form-control"}),
            'date_add': forms.SelectDateWidget(),
        }

class BlogLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'rows': 1, 'class': "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'rows': 1, 'class': "form-control"}))
    field_order = ['username', 'password']


class AddCommentForm(forms.ModelForm):
    """form for comments"""
    class Meta:
        model = Comments
        fields = ('name_user', 'content')
