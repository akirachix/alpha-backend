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
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from transaction.models import Transaction
from design_review.models import DesignReview
from decimal import Decimal


class TransactionAPITestCase(APITestCase):
    def setUp(self):
        self.transaction1 = Transaction.objects.create(
            amount=Decimal("100.00"),
            platform_fee=Decimal("5.00")
        )
        self.transaction2 = Transaction.objects.create(
            amount=Decimal("200.00"),
            platform_fee=Decimal("10.00")
        )
        self.transaction_list_url = reverse('transaction-list')
        self.transaction_detail_url = reverse('transaction-detail', kwargs={'pk': self.transaction1.pk})

    def test_get_transaction_list(self):
        response = self.client.get(self.transaction_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_transaction_detail(self):
        response = self.client.get(self.transaction_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Decimal(response.data['amount']), Decimal("100.00"))
        self.assertEqual(Decimal(response.data['platform_fee']), Decimal("5.00"))

    def test_create_transaction(self):
        data = {
            'amount': "150.00",
            'platform_fee': "7.50"
        }
        response = self.client.post(self.transaction_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 3)
        self.assertEqual(Decimal(response.data['amount']), Decimal("150.00"))

    def test_update_transaction(self):
        data = {
            'amount': "300.00",
            'platform_fee': "15.00"
        }
        response = self.client.put(self.transaction_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.transaction1.refresh_from_db()
        self.assertEqual(self.transaction1.amount, Decimal("300.00"))
        self.assertEqual(self.transaction1.platform_fee, Decimal("15.00"))

    def test_delete_transaction(self):
        response = self.client.delete(self.transaction_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertFalse(Transaction.objects.filter(pk=self.transaction1.pk).exists())


class DesignReviewAPITestCase(APITestCase):
    def setUp(self):
        
        self.design_review1 = DesignReview.objects.create(
            rating_value=5,
            comment="Great design!"
        )
        self.design_review2 = DesignReview.objects.create(
            rating_value=3,
            comment="Needs improvement"
        )
        self.design_review_list_url = reverse('design_review-list')
        self.design_review_detail_url = reverse('design_review-detail', kwargs={'pk': self.design_review1.pk})

    def test_get_design_review_list(self):
        response = self.client.get(self.design_review_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_design_review_detail(self):
        response = self.client.get(self.design_review_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rating_value'], 5)
        self.assertEqual(response.data['comment'], "Great design!")

    def test_create_design_review(self):
        data = {
            'rating_value': 4,
            'comment': "Good work"
        }
        response = self.client.post(self.design_review_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DesignReview.objects.count(), 3)
        self.assertEqual(response.data['rating_value'], 4)

    def test_update_design_review(self):
        data = {
            'rating_value': 2,
            'comment': "Updated comment"
        }
        response = self.client.put(self.design_review_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.design_review1.refresh_from_db()
        self.assertEqual(self.design_review1.rating_value, 2)
        self.assertEqual(self.design_review1.comment, "Updated comment")

    def test_delete_design_review(self):
        response = self.client.delete(self.design_review_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(DesignReview.objects.count(), 1)
        self.assertFalse(DesignReview.objects.filter(pk=self.design_review1.pk).exists())




