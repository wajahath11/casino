from django.urls import path
from .views import HomeView, CricketView, LoginView, CreateAccountView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cricket/', CricketView.as_view(), name='cricket'),
    path('login/', LoginView.as_view(), name='login'),
    path('create-account/', CreateAccountView.as_view(), name='create-account'),
]
