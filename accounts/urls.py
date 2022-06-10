from accounts.views import UserCreationView
from django.urls import path 
import django.contrib.auth.views as auth_views
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',UserCreationView.as_view(),name='sign_up'),
    path('password_change/',auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
]

