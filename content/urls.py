from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .views import home,register,login_auth


urlpatterns =[
    path('', home, name='home'),
    path('register',register , name='register'),
    path('login',login_auth, name='login'),
]

urlpatterns += static(settings.STATIC_URL,documents_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=[
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="register/password_reset_email.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="register/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="register/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="register/password_reset_complete.html"), name='password_reset_complete'),
]