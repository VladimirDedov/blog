from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<slug:slug>/', BlogDetail.as_view(), name='blog_detail'),
    path('distionary/', distionary, name='distionary'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('resume/', resume, name='resume'),
    path('distionary/<slug:word_slug>/', DetailWord.as_view(), name='detail_word'),
    path('add_word/', AddWord.as_view(), name='add_word'),
    path('add_post', add_post, name='add_post')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)  # Будет раздавать медиа файлы при вкл DEBAG. Без этого картинок из vedia не будет!
