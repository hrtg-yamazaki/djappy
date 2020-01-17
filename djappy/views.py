from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Article

# Create your views here.
class IndexView(generic.ListView):
    model = Article
    paginate_by = 6

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')

class DetailView(generic.DetailView):
    model = Article
