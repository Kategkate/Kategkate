from django.urls import path

from .views import UserUpdateView, update_profile_view
urlpatterns = [
    path('profile/', UserUpdateView.as_view(), name='user_update'),
    path('profile_update/', update_profile_view, name='profile_update'),
]
