from rest_framework import generics, views, viewsets, status, permissions
from rest_framework.response import Response
from .serializers import TodoCreateSerializer, TodoListSerializer, TodoUpdateSerializer
from apps.todo.models import Todo
from rest_framework.decorators import action


class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')


class TodoDetailView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer
    lookup_field = 'pk'
    permission_classes = (permissions.AllowAny)


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


