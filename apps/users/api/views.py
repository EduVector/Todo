from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserListSerializer
from apps.users.models import Account


class RegisterView(generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class UserListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAuthenticated]