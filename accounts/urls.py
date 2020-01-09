from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]