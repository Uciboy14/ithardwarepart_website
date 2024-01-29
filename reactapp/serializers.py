# serializers.py
from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import Category, Product, Cart, CartItem, Order, CustomUser

UserModel = get_user_model()

print(UserModel)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        print("********Create*******")
        print(validated_data)
        user_obj = UserModel.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
        user_obj.username = validated_data['email']
        user_obj.save()
        print("USer:", user_obj)
        return user_obj

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def check_user(self, clean_data):
        print(clean_data)
        print(UserModel)
        user = authenticate(username=clean_data['email'], password=clean_data['password'])
        print(user)
        if not user:
            raise ValidationError('user not found')
        return user

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('email', 'username')
