from django.contrib import admin
from .models import *
from .forms import *
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание')

    class Meta:
        model = Blog
        fields = '__all__'


@admin.register(Distionary)
class AdminDistionary(admin.ModelAdmin):
    list_display = ('id', 'word_eng', 'slug', 'word_rus', 'exemple_1_eng', 'exemple_1_rus', 'image')
    prepopulated_fields = {'slug': ('word_eng',)}


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'date_add')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('title', 'slug')
    list_editable = ('date_add',)
    form = BlogAdminForm


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'category', 'slug_category')
    prepopulated_fields = {'slug_category': ('category',)}


@admin.register(Comments)
class AdminComments(admin.ModelAdmin):
    list_display = ('name_user', 'content')
