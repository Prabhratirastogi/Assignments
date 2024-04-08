from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.models import User
from .models import Product
from .serializers import ProductsSerializer

def validate_password(value):
    if len(value) < 8:
        raise ValidationError('Password must be at least 8 characters long.')
    if not re.search(r'\d', value):
        raise ValidationError('Password must contain at least one digit.')
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
        raise ValidationError('Password must contain at least one special character.')

class UserCreate(APIView):
    def get(self, request):
        users = User.objects.all()
        user_data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
        return Response(user_data)
    
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            validate_email(email)
            validate_password(password)
        except ValidationError as e:
            return Response({'error': str(e)}, status=400)
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already taken'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({'message': 'User created successfully'}, status=201)

class UserDetail(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        get_user_data = {'id': user.id, 'username': user.username, 'email': user.email}
        return Response(get_user_data)

    def put(self, request, pk):
        user = get_object_or_404(User, id=pk)
        data = request.data
        user.username = data.get('username', user.username)
        if User.objects.filter(username=user.username).exclude(id=user.id).exists():
            return Response({'error': 'Username already taken'}, status=400)
        user.email = data.get('email', user.email)
        
        user.save()
        return Response({'message': 'User updated successfully'})

    def delete(self, request, pk):
        user = get_object_or_404(User, id=pk)
        user.delete()
        return Response({'message': 'User deleted successfully'},status=204)

class ProductsList(APIView):
    def get(self, request):
        products_list = Product.objects.all()
        serializer = ProductsSerializer(products_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Products Added Successfully'}, status=201)
        return Response(serializer.errors, status=400)

class ProductsDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product Updated Successfully'}, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response({'message': 'Product deleted successfully'}, status=204)
