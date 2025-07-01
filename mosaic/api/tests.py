from django.test import TestCase
# Create your tests here.

# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from users.models import Users
# from order.models import Order
# from datetime import date

# class UsersAPITest(APITestCase):
#     def setUp(self):
#         self.user = Users.objects.create(
#             full_name="Test User",
#             email="testuser@example.com",
#             latitude=0.0,      # Add required fields
#             longitude=0.0,     # Add required fields
#             # ...add all other required fields from your Users model here...
#         )

#     def test_list_users(self):
#         url = reverse('users-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_create_user(self):
#         url = reverse('users-list')
#         data = {
#             "full_name": "Another User",
#             "email": "another@example.com",
#             "latitude": 1.0,
#             "longitude": 1.0,
#             # ...add all other required fields from your Users model here...
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# class OrderAPITest(APITestCase):
#     def setUp(self):
#         self.order = Order.objects.create(
#             user_type='designer',
#             order_date=date.today(),
#             delivery_method="Courier",
#             total_price=150.25,
#             order_status="Pending"
#         )

#     def test_list_orders(self):
#         url = reverse('order-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_create_order(self):
#         url = reverse('order-list')
#         data = {
#             "user_type": "trader",
#             "order_date": str(date.today()),
#             "delivery_method": "Express",
#             "total_price": "200.50",
#             "order_status": "Processing"
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)



from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import Users
from order.models import Order
from datetime import date

class UsersAPITest(APITestCase):
    def setUp(self):
        self.user = Users.objects.create(
            full_name="Test User",
            email="testuser@example.com",
            phone_number="1234567890",
            password="securepassword",
            latitude=12.34,
            longitude=56.78,
            user_type="Designer"
        )

    def test_list_users(self):
        url = reverse('users-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        url = reverse('users-list')
        data = {
            "full_name": "Another User",
            "email": "another@example.com",
            "phone_number": "0987654321",
            "password": "anothersecurepassword",
            "latitude": 11.11,
            "longitude": 22.22,
            "user_type": "Trader"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class OrderAPITest(APITestCase):
    def setUp(self):
        self.user = Users.objects.create(
            full_name="Order User",
            email="orderuser@example.com",
            phone_number="1122334455",
            password="orderpassword",
            latitude=1.23,
            longitude=4.56,
            user_type="Trader"
        )
        self.order = Order.objects.create(
            user_type='designer',
            order_date=date.today(),
            delivery_method="Courier",
            total_price=150.25,
            order_status="Pending"
        )

    def test_list_orders(self):
        url = reverse('order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_order(self):
        url = reverse('order-list')
        data = {
            "user_type": "trader",
            "order_date": str(date.today()),
            "delivery_method": "Express",
            "total_price": "200.50",
            "order_status": "Processing"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)































# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from users.models import Users
# from order.models import Order
# from datetime import date

# class UsersAPITest(APITestCase):
#     def setUp(self):
#         self.user = Users.objects.create(
#             # Add required fields for your Users model initialization
#             # Example (replace with your actual fields):
#             full_name="Test User",
#             email="testuser@example.com",
#             # ... other required fields ...
#         )

#     def test_list_users(self):
#         url = reverse('users-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_create_user(self):
#         url = reverse('users-list')
#         data = {
#             "full_name": "Another User",
#             "email": "another@example.com",
#             # ... other required fields ...
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# class OrderAPITest(APITestCase):
#     def setUp(self):
#         self.user = Users.objects.create(
#             # Add required fields for your Users model initialization
#             full_name="Order User",
#             email="orderuser@example.com",
#             # ... other required fields ...
#         )
#         self.order = Order.objects.create(
#             user_type='designer',
#             order_date=date.today(),
#             delivery_method="Courier",
#             total_price=150.25,
#             order_status="Pending"
#             # If there is a ForeignKey to Users, add it here: user=self.user
#         )

#     def test_list_orders(self):
#         url = reverse('order-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_create_order(self):
#         url = reverse('order-list')
#         data = {
#             "user_type": "trader",
#             "order_date": str(date.today()),
#             "delivery_method": "Express",
#             "total_price": "200.50",
#             "order_status": "Processing"
#             # If there is a ForeignKey to Users, add user field: "user": self.user.id
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)