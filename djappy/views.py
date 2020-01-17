from django.shortcuts import render
from django.views import generic
from .models import Article

# Create your views here.
class IndexView(generic.ListView):
    model = Article
    paginate_by = 6