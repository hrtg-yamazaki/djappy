from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from djappy.models import Article
from .models import Profile
from .forms import UserSearchForm


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


def search(request):
    searchForm = UserSearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        object_list = User.objects.filter(
          Q(profile__nickname__contains=keyword) |
          Q(username=keyword)
        )
        context = {
            'message': 'ユーザーの検索',
            'object_list': object_list,
            'searchForm': searchForm,
            'comment': 'キーワードをニックネームに含むユーザー、ユーザー名が一致するユーザーはいません。',
        }
    else:
        searchForm = UserSearchForm()
        context = {
            'message': 'ユーザーの検索',
            'searchForm': searchForm,
            'comment': '検索結果はここに表示されます。ニックネームの部分一致、ユーザー名の完全一致による検索ができます。',
        }

    return render(request, 'accounts/user_search.html', context)


def logout_confirm(request):
    context = {
        'message': 'ログアウト確認',
        'comment': 'ログアウトしてよろしいですか？',
    }

    return render(request, 'accounts/logout_confirm.html', context)