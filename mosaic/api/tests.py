from rest_framework.test import APITestCase
from django.urls import reverse

class UsersAPITestCase(APITestCase):
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
        self.base_url = reverse('users-list')        
    def create_user(self):
        response = self.client.post(self.base_url, self.user_data, format='json')
        self.assertEqual(response.data['email'], self.user_data['email'])
    def read_user_list(self):
        response = self.client.get(self.base_url)
        self.assertGreaterEqual(len(response.data), 1)
    def read_single_user(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.data['email'], self.user_data['email'])
    def update_user(self):
        updated_data['email'] = 'maxrobi123@gmail.com'
        updated_data['full_name'] = 'Maxton Robinson'
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.data['email'], 'maxrobi123@gmail.com')
    def delete_user(self):
        response = self.client.delete(self.detail_url)
        self.assertFalse(Users.objects.filter(id=self.user.id).exists())
    