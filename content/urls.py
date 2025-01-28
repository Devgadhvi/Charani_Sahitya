from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home,register,login

urlpatterns =[
    path('', home, name='home'),
    path('register',register , name='register'),
    path('login',login, name='login')
]

urlpatterns += static(settings.STATIC_URL,documents_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)