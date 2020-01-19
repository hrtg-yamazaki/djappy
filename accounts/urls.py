from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='detail'),
]
