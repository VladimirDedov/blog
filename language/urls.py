from django.urls import path
from .views import *
urlpatterns = [
    path('', index,  name='index'),
    path('blog/', blog, name='blog'),
    path('distionary/', distionary, name='distionary')
]
