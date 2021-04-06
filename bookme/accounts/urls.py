from django.urls import path

from .views import UserUpdateView
urlpatterns = [
    path('profile/', UserUpdateView.as_view(), name='user_update'),
]
