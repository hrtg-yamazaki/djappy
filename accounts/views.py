from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from djappy.models import Article
from .models import Profile


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class UserDetailView(generic.DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['user_articles'] = Article.objects.filter(author_id=self.kwargs.get('pk'))
        return context


class ProfileCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Profile
    fields = ['nickname', 'gender', 'introduction']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreateView, self).form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Profile
    fields = ['nickname', 'gender', 'introduction']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied('編集権限がありません')
        return super(ProfileUpdateView, self).dispatch(request, *args, **kwargs)
