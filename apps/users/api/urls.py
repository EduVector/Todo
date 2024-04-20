from django.urls import path
from .views import RegisterView, UserListView, LoginAPIView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('UserList/', UserListView.as_view()),
]