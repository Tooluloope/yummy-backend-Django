from django.shortcuts import render
from knox.models import AuthToken


# Create your views here.
from rest_framework import viewsets,generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from knox.auth import TokenAuthentication
from .permissions import IsPostOrIsAuthenticated

from rest_framework.response import Response

from .serializers import PizzaSerializer, OrderSerializer, UserSerializer, RegisterSerializer, LoginSerializer
from .models import Pizza, Order




class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all().order_by('id')
    serializer_class = PizzaSerializer

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsPostOrIsAuthenticated,]

    serializer_class = OrderSerializer

    queryset = Order.objects.all().order_by('id')


class UserAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        _, token = AuthToken.objects.create(user)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token
        })


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token
        })

