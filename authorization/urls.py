from django.urls import path
from .views import register_user
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    # path('register/', register_user, name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
]
