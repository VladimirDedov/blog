from django.urls import path
from .views import *
urlpatterns = [
    path('', index,  name='index'),
    path('blog/', blog, name='blog'),
    path('distionary/', distionary, name='distionary'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('resume/', resume, name='resume'),
    path('distionary/<slug:word_slug>/', DetailWord.as_view(), name='detail_word'),
    path('add_word/', AddWord.as_view(), name='add_word'),
]
