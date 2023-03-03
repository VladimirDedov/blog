from django.urls import reverse
from django.db import models


class Distionary(models.Model):
    """model for distionary of words"""
    word_eng = models.CharField(max_length=255, db_index=True, verbose_name='Английское слово')
    slug = models.SlugField(unique=True, max_length=255, db_index=True, verbose_name='URL')
    word_rus = models.CharField(max_length=255, db_index=True, verbose_name='Русское слово')
    exemple_1_eng = models.TextField(blank=True, verbose_name='Пример_1_Анг')
    exemple_1_rus = models.TextField(blank=True, verbose_name='Пример_1_Рус')
    exemple_2_eng = models.TextField(blank=True, verbose_name='Пример_2_Анг')
    exemple_2_rus = models.TextField(blank=True, verbose_name='Пример_2_Рус')
    exemple_3_eng = models.TextField(blank=True, verbose_name='Пример_3_Анг')
    exemple_3_rus = models.TextField(blank=True, verbose_name='Пример_3_Рус')
    image = models.ImageField(blank=True, upload_to='image/%y/%m/%d', verbose_name='Картинка')

    def __str__(self):
        return self.word_eng

    class META:
        verbose_name = 'Словарь'
        verbose_name_plural = 'Словари'

    def get_absolut_url(self):
        return reverse('detail_word', kwargs={'word_slug': self.slug})
