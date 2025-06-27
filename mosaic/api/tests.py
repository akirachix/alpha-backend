from rest_framework.test import APITestCase
from rest_framework import status
from users.models import Users
class UserAPITestCase(APITestCase):
   def setUp(self):
       self.user_data = {
           full_name="Paoli Endric",
           email="paoli23red@gmail.com",
           phone_number="0737845625",
           password="paolire384",
           latitude="4.0",
           longitude="3.0",
           user_type="Designer"
       }
       self.users = Users.objects.create(**self.user_data)
       self.url = "/api/users/"

   def test_get_user(self):
       response = self.client.get(f"{self.url}{self.users.id}/", format="json")
       self.assertEqual(response.status_code, status.HTTP_200_OK)
   def test_update_user(self):
       updated_data = self.user_data.copy()
       updated_data["full_name"] = "Paoli Endric"
       response = self.client.put(f"{self.url}{self.users.id}/", updated_data, format="json")
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.assertEqual(response.data["full_name"], "Paolina Sandra")
   def test_delete_user(self):
       response = self.client.delete(f"{self.url}{self.users.user_id}/")
       self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    