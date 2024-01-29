from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer, CategorySerializer, ProductSerializer, CartSerializer, CartItemSerializer, OrderSerializer  
from .models import Category, Product, Cart, CartItem, Order
from rest_framework import permissions, status, generics
from .validations import custom_validation, validate_email, validate_password
import json

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # Assuming 'id' is the name of the field you use for product IDs

class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UserRegister(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		# Get the JSON string from the QueryDict
		json_string = list(request.data.keys())[0]
		
		# Parse the JSON string into a dictionary
		data = json.loads(json_string)
		
		clean_data = custom_validation(data)
		print("*************PASSED***********")
		print(clean_data)
		serializer = UserRegisterSerializer(data=clean_data)
		if serializer.is_valid(raise_exception=True):
			print("********YES**********")
			user = serializer.create(clean_data)
			if user:
				# Generate a token for the user
				refresh = RefreshToken.for_user(user)
		
				print("***********USER**********", user)
				# Include success message in the response
				response_data = {
                'success': True,
                'data': serializer.data,
				'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
            }
				return Response(response_data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	##
	def post(self, request):
		data = request.data
		print("*******LOGIN DETAILS********")
		# Get the JSON string from the QueryDict
		json_string = list(request.data.keys())[0]
		
		# Parse the JSON string into a dictionary
		data = json.loads(json_string)
		print("********DATA**********")
		print(data)
		assert validate_email(data)
		assert validate_password(data)
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			login(request, user)

			# Generate a token for the user
			refresh = RefreshToken.for_user(user)
	
			# Include success message in the response
			response_data = {
				'success': True,
                'data': serializer.data,
				'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
            }
			return Response(response_data, status=status.HTTP_200_OK)


class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		response_data = {
				'success': True,
            }
		return Response(response_data, status=status.HTTP_200_OK)


class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	##
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)