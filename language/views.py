from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView
from .models import *
from .forms import AddWordForm

main_menu = [
    {'title': 'Домашняя', 'url_name': 'index'},
    {'title': 'Резюме', 'url_name': 'resume'},
    {'title': 'Блог', 'url_name': 'blog'},
    {'title': 'Словарь', 'url_name': 'distionary'},
    {'title': 'Обо мне', 'url_name': 'about'},
    {'title': 'Контакты', 'url_name': 'contact'},
    {'title': 'Слово', 'url_name': 'add_word'},
    {'title': 'Добавить пост', 'url_name': 'add_post'}
]


def index(request):
    """Home page"""
    context = {'menu': main_menu, 'flag': 'index', 'title': 'Главная страница'}
    return render(request, 'blog/index.html', context=context)


def blog(request):
    blog = Blog.objects.all().order_by('-date_add')[:4]
    context = {'menu': main_menu, 'flag': 'blog', 'title': 'Блог', 'blog_list': blog}
    return render(request, 'blog/blog.html', context=context)


class BlogDetail(DetailView):
    """shoe the detail of the selected blog"""
    model = Blog
    template_name = 'blog/detail_blog.html'
    context_object_name = 'blog'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Blog.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = main_menu
        context['title'] = 'Почитать'
        context['cat_selected'] = Blog.objects.get(slug=self.kwargs['slug'])
        return context


class ShowCategory(ListView):
    """show sorted list of detail blogs"""
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        return Blog.objects.filter(category__slug_category=self.kwargs['slug_category'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = main_menu
        context['title'] = 'Почитать'
        context['cat_selected'] = Category.objects.get(slug_category=self.kwargs['slug_category'])
        return context


def add_post(request):
    return HttpResponse("Add post")


def distionary(request):
    """distionary of english worlds"""
    words = Distionary.objects.all()
    context = {'menu': main_menu, 'flag': 'distionary', 'words': words, 'title': 'Словарь'}
    return render(request, 'blog/distionary.html', context=context)


class DetailWord(DetailView):
    """show the details of the selected word"""
    model = Distionary
    template_name = 'blog/detail_word.html'
    slug_url_kwarg = 'word_slug'
    context_object_name = 'detail_word'

    def get_queryset(self):
        return Distionary.objects.filter(slug=self.kwargs['word_slug']).order_by('word_eng')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = main_menu
        context['title'] = Distionary.objects.filter(slug=self.kwargs['word_slug'])[0]
        print(context)
        return context


class AddWord(CreateView):
    """Add word in distionary"""
    form_class = AddWordForm
    template_name = 'blog/add_word.html'
    success_url = reverse_lazy('distionary')  # расскоментировать позже. Перенаправления get_absolute_url из модели

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = main_menu
        context['title'] = 'Добавить слово'
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
