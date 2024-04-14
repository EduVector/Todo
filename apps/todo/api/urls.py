from django.urls import path
from .views import TodoCreateView, TodoListView, TodoDetailView, TodoUpdateView, TodoDeleteView, \
                TodoRUDView, TodoListCreateView


urlpatterns = [
    path('TodoCreate/', TodoCreateView.as_view()),
    path('TodoList/', TodoListView.as_view()),
    path('TodoDetail/<int:pk>/', TodoDetailView.as_view()),
    path('TodoUpdate/<int:pk>/', TodoUpdateView.as_view()),
    path('TodoDestroy/<int:pk>/', TodoDeleteView.as_view()),


    path('TodoRUD/<int:pk>/', TodoRUDView.as_view()),
    path('Todo/', TodoListCreateView.as_view()),
]