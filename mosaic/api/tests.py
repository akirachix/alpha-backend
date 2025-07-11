<<<<<<< HEAD
from rest_framework.test import APITestCase
from django.urls import reverse
from django.test import TestCase
from users.models import Users

class UsersAPITestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            'full_name': 'Max Robinson',
            'email': 'maxrob456@gmail.com',
            'phone_number': '0762384756',
            'password': 'maxinmall23',
            'latitude': 5.0,
            'longitude': 4.0,
            'user_type': 'Designer'
        }
        self.user = Users.objects.create(**self.user_data)
        self.base_url = reverse('users-list')
        self.detail_url = reverse('users-detail', args=[self.user.id])
    def test_create_user(self):
        response = self.client.post(self.base_url, self.user_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['email'], self.user_data['email'])
    def test_read_user_list(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
    def test_read_single_user(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['email'], self.user_data['email'])
    def test_update_user(self):
        updated_data = self.user_data.copy()
        updated_data['email'] = 'maxrobi123@gmail.com'
        updated_data['full_name'] = 'Maxton Robinson'
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['email'], 'maxrobi123@gmail.com')
    def test_delete_user(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Users.objects.filter(id=self.user.id).exists())


class UsersModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'full_name': 'Max Robinson',
            'email': 'maxrob145@gmail.com',
            'phone_number': '0762384756',
            'password': 'maxinmall23',
            'latitude': 5.0,
            'longitude': 4.0,
            'user_type': 'Designer'
        }
    def test_create_user(self):
        user = Users.objects.create(**self.user_data)
        self.assertEqual(user.full_name, 'Max Robinson')
        self.assertEqual(user.email, 'maxrob145@gmail.com')
        self.assertTrue(Users.objects.filter(id=user.id).exists())
    def test_get_user(self):
        user = Users.objects.create(**self.user_data)
        fetched_user = Users.objects.get(id=user.id)
        self.assertEqual(fetched_user.phone_number, '0762384756')
        self.assertEqual(fetched_user.user_type, 'Designer')
    def test_update_user(self):
        user = Users.objects.create(**self.user_data)
        user.full_name = 'Maxwell Rob'
        user.phone_number = '0712345678'
        user.save()
        updated_user = Users.objects.get(id=user.id)
    def test_delete_user(self):
        user = Users.objects.create(**self.user_data)
        user_id = user.id
        user.delete()
        self.assertFalse(Users.objects.filter(id=user_id).exists())

from django.test import TestCase



