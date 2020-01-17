from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .models import Article


class IndexView(generic.ListView):
    model = Article
    paginate_by = 6

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')

class DetailView(generic.DetailView):
    model = Article

class CreateView(generic.edit.CreateView):
    model = Article
    fields = '__all__'

class UpdateView(generic.edit.UpdateView):
    model = Article
    fields = '__all__'

class DeleteView(generic.edit.DeleteView):
    model = Article
    success_url = reverse_lazy('djappy:index')