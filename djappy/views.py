from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import Article, Category, Comment
from .forms import TitleSearchForm, CategorySearchForm


class IndexView(generic.ListView):
    model = Article
    paginate_by = 6

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')


class DetailView(generic.DetailView):
    model = Article
    
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(article_id=self.kwargs.get('pk'))
        return context
    


class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Article
    fields = ['title', 'category', 'image', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)


class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Article
    fields = ['title', 'category', 'image', 'content']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('編集権限がありません')
        return super(UpdateView, self).dispatch(request, *args, **kwargs)


class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Article
    success_url = reverse_lazy('djappy:index')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('削除権限がありません')
        return super(DeleteView, self).dispatch(request, *args, **kwargs)


def search_title(request):
    searchForm = TitleSearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        object_list = Article.objects.filter(title__contains=keyword).order_by('-created_at')
        context = {
            'message': '記事の検索',
            'object_list': object_list,
            'searchForm': searchForm,
            'comment': 'タイトルをキーワードに含む記事はありません',
        }
    else:
        searchForm = TitleSearchForm()
        context = {
            'message': '記事の検索',
            'searchForm': searchForm,
            'comment': 'ヒットした記事がここに表示されます',
        }

    return render(request, 'djappy/search_title.html', context)


def search_category(request):
    searchForm = CategorySearchForm(request.GET)
    if searchForm.is_valid():
        id = searchForm.cleaned_data['category_id']
        object_list = Article.objects.filter(category_id=id).order_by('-created_at')
        context = {
            'message': '記事の検索',
            'object_list': object_list,
            'searchForm': searchForm,
            'comment': 'タイトルをキーワードに含む記事はありません',
        }
    else:
        searchForm = CategorySearchForm()
        context = {
            'message': '記事の検索',
            'searchForm': searchForm,
            'comment': 'ヒットした記事がここに表示されます',
        }

    return render(request, 'djappy/search_category.html', context)


class CommentCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Comment

    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        article_pk = self.kwargs.get('pk')
        form.instance.article = Article.objects.get(pk=article_pk)
        return super(CommentCreateView, self).form_valid(form)


class CommentDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Comment
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('削除権限がありません')
        return super(CommentDeleteView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        obj = self.get_object()
        article_pk = obj.article_id
        return reverse("djappy:detail", kwargs={"pk": article_pk})
