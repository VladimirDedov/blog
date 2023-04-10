from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

serializers_path = [
    path('api/v1/blog/', BlogListView.as_view()),
    path('api/v1/blog/<slug:slug>/', BlogDetailView.as_view()),
    path('api/v1/dictionary/', DictListView.as_view()),
    path('api/v1/dictionary/<slug:slug>/', DetailWordView.as_view()),
]

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('blog/', ShowBlog.as_view(), name='blog'),
    path('blog/<slug:slug>/', BlogDetail.as_view(), name='blog_detail'),
    path('distionary/', DictionaryList.as_view(), name='distionary'),
    path('distionary/<slug:word_slug>/', DetailWord.as_view(), name='detail_word'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('resume/', resume, name='resume'),
    path('add_word/', AddWord.as_view(), name='add_word'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('category/<slug:slug_category>/', ShowCategory.as_view(), name='category'),
    path('comments/<int:pk>/', AddComment.as_view(), name='add_comment'),
    path('login/', BlogLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='log_out'),
] + serializers_path

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)  # Будет раздавать медиа файлы при вкл DEBAG. Без этого картинок из media не будет!
