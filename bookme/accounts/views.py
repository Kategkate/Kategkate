from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.shortcuts import render

from django.views.generic import UpdateView, CreateView

from accounts.forms import UserUpdateForm, ProfileFormset


# LoginRequiredMixin добавляет проверку того, что пользователь авторизован в системе


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/user_update.html'
    # отвечает за импорт модели пользователя
    model = get_user_model()
    form_class = UserUpdateForm
    success_url = '/'
    login_url = '/admin/login'

    def get_object(self, queryset=None):
        return self.request.user


def update_profile_view(request):
    if request.method == 'POST':
        formset = ProfileFormset(request.POST, request.FILES, instance= request.user)
        if formset.is_valid():
            profile = formset.save()
            print(profile)
        print(formset.errors)
    else:
        formset = ProfileFormset()
    return render(request, 'profile_update.html', {'formset': formset})
