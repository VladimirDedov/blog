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
    image = models.ImageField(blank=True, upload_to='word/image/%y/%m/%d', verbose_name='Картинка')

    class META:
        verbose_name = 'Словарь'
        verbose_name_plural = 'Словари'
        ordering = ['word_eng']

    def __str__(self):
        return self.word_eng

    def get_absolute_url(self):
        return reverse('detail_word', kwargs={'word_slug': self.slug})


class Category(models.Model):
    """model for category of blog"""
    category = models.CharField(max_length=255, verbose_name='Категория')
    slug_category = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug_category': self.slug_category})


class Blog(models.Model):
    """model for blog detail"""
    title = models.CharField(max_length=255, verbose_name='Заголовок блога')
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True, db_index=True)
    content = models.TextField(verbose_name='Содержание')
    date_add = models.DateField(verbose_name="Дата создания")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    image_1 = models.ImageField(blank=True, upload_to='blog/image/%y/%m/%d', verbose_name='Главная картинка')
    image_2 = models.ImageField(blank=True, upload_to='blog/image/%y/%m/%d', verbose_name='Картинка 2')
    image_3 = models.ImageField(blank=True, upload_to='blog/image/%y/%m/%d', verbose_name='Картинка 3')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})


class Comments(models.Model):
    """model for comments of user"""
    name_user = models.CharField(max_length=255, verbose_name='Имя пользователя')
    content = models.TextField(verbose_name='Комментария')
    blog = models.ForeignKey('Blog', on_delete=models.PROTECT, verbose_name='Блог')
