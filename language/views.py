from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView
from .models import *
from .utils import *
from .forms import AddWordForm, AddPostForm, BlogLoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout


class Index(DataMixin, ListView):
    """main page"""
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'blog'

    def get_queryset(self):
        return Blog.objects.all().last()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница', flag='index')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ShowBlog(DataMixin, ListView):
    """show list blog"""
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blog_list'
    paginate_by = 1

    def get_queryset(self):
        queries = Blog.objects.filter(is_published=True).order_by('-date_add')[:4]
        return queries

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Блог', flag='blog')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class BlogDetail(DataMixin, DetailView):
    """shoe the detail of the selected blog"""
    model = Blog
    template_name = 'blog/detail_blog.html'
    context_object_name = 'blog'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Blog.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Почитать', cat_selected=Blog.objects.get(slug=self.kwargs['slug']))
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ShowCategory(DataMixin, ListView):
    """show sorted list of detail blogs"""
    paginate_by = 2
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        return Blog.objects.filter(category__slug_category=self.kwargs['slug_category'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = Category.objects.get(slug_category=self.kwargs['slug_category'])
        c_def = self.get_user_context(title=title, cat_selected=title)
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class Distionary(DataMixin, ListView):
    """distyonary of english worlds"""
    model = Distionary
    template_name = 'blog/distionary.html'
    context_object_name = 'words'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Словарь', flag='distionary')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class DetailWord(DataMixin, DetailView):
    """show the details of the selected word"""
    model = Distionary
    template_name = 'blog/detail_word.html'
    slug_url_kwarg = 'word_slug'
    context_object_name = 'detail_word'

    def get_queryset(self):
        return Distionary.objects.filter(slug=self.kwargs['word_slug']).order_by('word_eng')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=Distionary.objects.filter(slug=self.kwargs['word_slug'])[0])
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AddWord(DataMixin,CreateView):
    """Add word in distionary"""
    form_class = AddWordForm
    template_name = 'blog/add_word.html'
    success_url = reverse_lazy('distionary')  # расскоментировать позже. Перенаправления get_absolute_url из модели

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить слово', flag='add_word')
        context = dict(list(context.items()) + list(c_def.items()))
        return context



class AddPost(DataMixin, CreateView):
    """add post in blog"""
    form_class = AddPostForm
    template_name = 'blog/add_post.html'
    success_url = reverse_lazy('blog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить пост', flag='add_post')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class BlogLoginView(LoginView):
    """class for authenfication"""
    form_class = BlogLoginForm
    template_name = 'blog/login.html'

    def get_success_url(self):
        return reverse_lazy('add_word')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = main_menu
        context['title'] = 'Авторизация'
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


def logout_user(request):
    logout(request)
    return redirect('index')
