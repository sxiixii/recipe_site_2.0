from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView

from .forms import CreationForm
from .models import Follow


class SignUpView(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')
    template_name = 'auth/registration.html'


class UserFollowView(LoginRequiredMixin, ListView):
    model = Follow
    paginate_by = settings.PAGINATE_BY
    template_name = 'users/user_follow.html'

    def get_queryset(self):
        """
        Возвращаем подписки текущего пользователя.
        """
        following = super().get_queryset()
        following = following.filter(user=self.request.user)
        return following