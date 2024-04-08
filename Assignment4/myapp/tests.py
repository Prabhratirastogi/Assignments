from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product

class UserCreateTestCase(APITestCase):
    def test_create_user(self):
        url = reverse('user-create')
        data = {'username': 'testuser', 'email': 'invalidemail', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)  # No user should be created

    def test_create_user_invalid_data(self):
        url = reverse('user-create')
        data = {'username': 'testuser', 'email': 'invalidemail', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)  # No user should be created

class UserDetailTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_get_user(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')

    def test_get_user_not_found(self):
        url = reverse('user-detail', args=[1000])  # Non-existent user id
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



class ProductsListTestCase(APITestCase):
    def test_get_products_list(self):
        url = reverse('products-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions to verify the response data

    def test_create_product(self):
        url = reverse('products-list')
        data = {'name': 'Test Product', 'description': 'Test Description', 'price': 9.99, 'quantity': 10}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        # Add more assertions to verify the created product details

class ProductsDetailTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.0, quantity=5)

    def test_get_product_detail(self):
        url = reverse('products-detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Product')

    def test_update_product(self):
        url = reverse('products-detail', args=[self.product.id])
        data = {'name': 'Updated Product', 'description': 'Updated Description', 'price': 15.0, 'quantity': 10}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')
        self.assertEqual(self.product.description, 'Updated Description')
        self.assertEqual(self.product.price, 15.0)
        self.assertEqual(self.product.quantity, 10)

    def test_delete_product(self):
        url = reverse('products-detail', args=[self.product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())
