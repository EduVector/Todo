from django.urls import path
from .views import RegisterView, UserListView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('UserList/', UserListView.as_view()),
]