from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home,song_list,song_detail

urlpatterns =[
    path('', home, name='home'),
    path('songs/', song_list, name='song_list'),
    path('songs/<int:id>/', song_detail, name='song_detail'),
]

urlpatterns += static(settings.STATIC_URL,documents_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)