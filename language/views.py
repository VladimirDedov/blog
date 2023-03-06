from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .models import *
from .forms import AddWordForm

main_menu = [
    {'title': 'Домашнаяя', 'url_name': 'index'},
    {'title': 'Резюме', 'url_name': 'resume'},
    {'title': 'Блог', 'url_name': 'blog'},
    {'title': 'Словарь', 'url_name': 'distionary'},
    {'title': 'Обо мне', 'url_name': 'about'},
    {'title': 'Контакты', 'url_name': 'contact'},
    {'title': 'Слово', 'url_name': 'add_word'}
]


def index(request):
    """Home page"""
    context = {'menu': main_menu, 'flag': 'index'}
    return render(request, 'blog/index.html', context=context)


def blog(request):
    context = {'menu': main_menu, 'flag': 'blog'}
    return render(request, 'blog/blog.html', context=context)


def distionary(request):
    """distionary of english worlds"""
    words = Distionary.objects.all()
    context = {'menu': main_menu, 'flag': 'distionary', 'words': words}
    return render(request, 'blog/distionary.html', context=context)


class DetailWord(DetailView):
    model = Distionary
    template_name = 'blog/detail_word.html'
    slug_url_kwarg = 'word_slug'
    context_object_name = 'detail_word'

    def get_queryset(self):
        return Distionary.objects.filter(slug=self.kwargs['word_slug']).order_by('word_eng')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = main_menu
        return context


class AddWord(CreateView):
    """Add word in distionary"""
    form_class = AddWordForm
    template_name = 'blog/add_word.html'
    success_url = reverse_lazy('distionary') #расскоментировать позже. Перенаправления get_absolute_url из модели

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = main_menu
        return context


def about(request):
    """About me page"""
    context = {'menu': main_menu, 'flag': 'about'}
    return render(request, 'blog/about.html', context=context)


def contact(request):
    context = {'menu': main_menu, 'flag': 'contact'}
    return render(request, 'blog/contact.html', context=context)


def resume(reauest):
    return redirect('http://dvv-res.ru')

# def detail_word(request, slug):
#     words = Distionary.objects.all()
#     context = {'menu': main_menu,
#                'flag': 'distionary'}
#     return render(request, 'blog/detail_word.html', context=context)
