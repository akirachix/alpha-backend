from django.test import TestCase
# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import Users
from order.models import Order
from datetime import date

class UsersAPITest(APITestCase):
    def setUp(self):
        self.user = Users.objects.create(
            full_name="Hasset Abera",
            email="hassetabera@gmail.com",
            phone_number="0934567890",
            password="hassetabera10",
            latitude=12.34,
            longitude=56.78,
            user_type="Trader"
        )

    def test_list_users(self):
        url = reverse('users-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        url = reverse('users-list')
        data = {
            "full_name": "Naol Wakjira",
            "email": "naolwakjira@gmail.com",
            "phone_number": "0987654321",
            "password": "naolwakjira10",
            "latitude": 11.11,
            "longitude": 22.22,
            "user_type": "Trader"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class OrderAPITest(APITestCase):
    def setUp(self):
        self.user = Users.objects.create(
            full_name="Netsi Abebe",
            email="netsiabebe@gmail.com",
            phone_number="0922334455",
            password="netsiabebe10",
            latitude=1.23,
            longitude=4.56,
            user_type="Trader"
        )
        self.order = Order.objects.create(
            user_type='Trader',
            order_date=date.today(),
            delivery_method="Pickup",
            total_price=150.25,
            order_status="Pending"
        )

    def test_list_orders(self):
        url = reverse('order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

 




















