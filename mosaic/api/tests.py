from django.test import TestCase
# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from order.models import Order
from datetime import date

class OrderAPITest(APITestCase):
    def setUp(self):

        self.order = Order.objects.create(
            order_date=date.today(),
            delivery_method="Pickup",
            total_price=150.25,
            order_status="Pending"
        )
        self.list_url = reverse('order-list')
        self.detail_url = reverse('order-detail', kwargs={'pk': self.order.pk})

        

    def test_create_order(self):
        data = {
            "order_date": str(date.today()),
            "delivery_method": "Delivery",
            "total_price": 200.50,
            "order_status": "Processing"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)
        self.assertEqual(response.data['delivery_method'], "Delivery")



    def test_list_orders(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)



    def test_retrieve_order(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['order_status'], self.order.order_status)



    def test_update_order(self):
        data = {
            "order_date": str(self.order.order_date),
            "delivery_method": "pickup",
            "total_price": 175.00,
            "order_status": "fulfilled"
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.delivery_method, "pickup")
        self.assertEqual(self.order.order_status, "fulfilled")



    def test_partial_update_order(self):
        data = {
            "order_status": "Delivered"
        }
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.order_status, "Delivered")



    def test_delete_order(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Order.objects.filter(pk=self.order.pk).exists())









