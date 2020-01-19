from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('users/<int:pk>', views.UserDetailView.as_view(), name='detail'),
    path('profile/create', views.ProfileCreateView.as_view(), name='create'),
    path('profile/<int:pk>/update', views.ProfileUpdateView.as_view(), name='update'),
    path('users/search', views.search, name='search'),
]
