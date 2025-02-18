from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .views import home,register,login_auth,profile,user_logout,ask_permissons,edit_profile,feedpage,creator_form,post_detail


urlpatterns =[
    path('', home, name='home'),
    path('register/',register , name='register'),
    path('login/',login_auth, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/',profile, name='profile'),
     path('profile/edit/', edit_profile, name='edit_profile'),
    path('send_email/<int:id>', ask_permissons, name='ask_permissons'),
    path('feed/', feedpage, name='feed'),
    path('create/', creator_form, name='create'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
]

urlpatterns += static(settings.STATIC_URL,documents_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=[
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="register/password_reset_email.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="register/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="register/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="register/password_reset_complete.html"), name='password_reset_complete'),
]