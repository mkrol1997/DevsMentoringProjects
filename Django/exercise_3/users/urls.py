from .views import ProfileView, UserRegisterView, UserLoginView
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('', UserLoginView.as_view(
         template_name='users/login.html',
         redirect_authenticated_user=True),
         name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', auth_views.LogoutView.as_view(
         template_name='users/logout.html'),
         name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
         template_name='pw_reset/pw_reset.html'),
         name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(
         template_name='pw_reset/pw_reset_done.html'),
         name='password_reset_done'),
    path('password_reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
         template_name='pw_reset/pw_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset/complete', auth_views.PasswordResetCompleteView.as_view(
         template_name='pw_reset/pw_reset_complete.html'),
         name='password_reset_complete'),
]
