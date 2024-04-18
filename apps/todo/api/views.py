from rest_framework import generics, views, viewsets, status
from rest_framework.response import Response
from .serializers import TodoCreateSerializer, TodoListSerializer, TodoUpdateSerializer
from apps.todo.models import Todo
from rest_framework.decorators import action


class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer


class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer



class TodoDetailView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer
    lookup_field = 'pk'


class TodoUpdateView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoUpdateSerializer
    lookup_field = 'pk'


class TodoDeleteView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    lookup_field = 'pk'


class TodoRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer
    lookup_field = 'pk'


class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer


# views

class TodoListAPIView(views.APIView):
    sz_class = TodoListSerializer

    def get(self, request, *args, **kwargs):
        queryset = Todo.objects.all()
        serializer = self.sz_class(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        pass


# viewsets
class TodoCRUDView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer


    @action(detail=False, methods=['get'])
    def get_todo_list(self, request):
        sz = self.get_serializer(self.queryset, many=True)
        return Response(sz.data)


