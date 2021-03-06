from django.urls import path
from . import views

app_name = 'djappy'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/update', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.DeleteView.as_view(), name='delete'),
    path('search/title', views.search_title, name='search_title'),
    path('search/category', views.search_category, name='search_category'),
    path('<int:pk>/comment/create', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='comment_delete'),
]