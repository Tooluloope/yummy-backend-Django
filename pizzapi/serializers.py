from rest_framework import serializers
from django.contrib.auth import authenticate



from .models import Pizza, Order, UserProfile

class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Pizza
        fields = ('id', 'url', 'name','price', 'desc')



class OrderSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Order
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'fullname')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'password','fullname')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            validated_data['email'],
             validated_data['fullname'],
            validated_data['username'],
            validated_data['password']
           
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        print(data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")