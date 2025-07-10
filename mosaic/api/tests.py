from django.test import TestCase
from shopping_cart.models import Shopping_cart
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class ShoppingCartTests(APITestCase):
   def setUp(self):
       self.Cart_data= Shopping_cart.objects.create(quantity=3, price=10.00)
      
   def test_get_shoppingCart(self):
       Shopping_cart.objects.create(**self.Cart_data)
       url=reverse ("shopping_cart-list")
       response=self.client.get(url)
       self.assertEqual(response.status_code, status.HTTP_200_OK)


   def test_put_shoppingCart(self):
       Shopping_cart.objects.create(**self.Cart_data)
       Shopping_cart=Shopping_cart.objects.first()
       url=reverse ("shopping_cart-list", args =[Shopping_cart.id])
       response=self.client.put(url,self.Shopping_cart_data, format="json")
       self.assertEqual(response.status_code, status.HTTP_200_OK)


   def test_delete_shoppingCart(self):
       Shopping_cart.objects.create(**self.Cart_data)
       Shopping_cart=Shopping_cart.objects.first()
       url=reverse ("shopping_cart-list", args =[Shopping_cart.id])
       response=self.client.delete(url)
       self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


   def test_post_shoppingCart(self):
      url=reverse("shopping_cart-list")
      response=self.client.post(url,self.Cart_data, format="json")
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)