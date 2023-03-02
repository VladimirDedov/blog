from django.shortcuts import render

def index(request):
    """Home page"""
    return render(request,'blog/index.html')

def blog(request):
    return render(request, 'blog/blog.html')

def distionary(request):
    """distionary of english worlds"""
    return render(request, 'blog/distionary.html')

def about(request):
    """About me page"""
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')