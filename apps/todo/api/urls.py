from django.urls import path
from .views import TodoCreateView, TodoListView, TodoDetailView, TodoUpdateView, TodoDeleteView, \
                TodoRUDView, TodoListCreateView, TodoListAPIView, TodoCRUDView

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('crud', TodoCRUDView, basename="todo-crud")



urlpatterns = [
    path('TodoCreate/', TodoCreateView.as_view()),
    path('TodoList/', TodoListView.as_view()),
    path('TodoDetail/<int:pk>/', TodoDetailView.as_view()),
    path('TodoUpdate/<int:pk>/', TodoUpdateView.as_view()),
    path('TodoDestroy/<int:pk>/', TodoDeleteView.as_view()),


    path('TodoRUD/<int:pk>/', TodoRUDView.as_view()),
    path('Todo/', TodoListCreateView.as_view()),

    # views
    path('todo-list/', TodoListAPIView.as_view())
] + router.urls