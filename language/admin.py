from django.contrib import admin
from .models import *
@admin.register(Distionary)
class AdminDistionary(admin.ModelAdmin):
    list_display = ('word_eng', 'slug','word_rus', 'exemple_1_eng','exemple_1_rus', 'exemple_2_eng','exemple_2_rus', 'exemple_3_eng','exemple_3_rus')
    prepopulated_fields ={'slug':('word_eng',)}

