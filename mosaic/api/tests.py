from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from transaction.models import Transaction
from design_review.models import DesignReview

class TransactionViewSetTests(APITestCase):
    def setUp(self):
        self.transaction_url = reverse('transaction-list')
        self.transaction_data = {
            'amount': 100.00,
            'description': 'Test transaction'
        }
        self.transaction = Transaction.objects.create(**self.transaction_data)

    def test_create_transaction(self):
        response = self.client.post(self.transaction_url, self.transaction_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 2)  # One existing + one created
        self.assertEqual(Transaction.objects.get(description='Test transaction').description, 'Test transaction')

    def test_get_transactions(self):
        response = self.client.get(self.transaction_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # One transaction exists

    def test_update_transaction(self):
        update_data = {
            'amount': 150.00,
            'description': 'Updated transaction'
        }
        response = self.client.put(reverse('transaction-detail', args=[self.transaction.id]), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.transaction.refresh_from_db()
        self.assertEqual(self.transaction.amount, 150.00)
        self.assertEqual(self.transaction.description, 'Updated transaction')

    def test_delete_transaction(self):
        response = self.client.delete(reverse('transaction-detail', args=[self.transaction.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Transaction.objects.count(), 0)  # Transaction should be deleted

class DesignReviewViewSetTests(APITestCase):
    def setUp(self):
        self.design_review_url = reverse('design_review-list')
        self.design_review_data = {
            'reviewer': 'John Doe',
            'comments': 'Looks good!'
        }
        self.design_review = DesignReview.objects.create(**self.design_review_data)

    def test_create_design_review(self):
        response = self.client.post(self.design_review_url, self.design_review_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DesignReview.objects.count(), 2)  # One existing + one created
        self.assertEqual(DesignReview.objects.get(comments='Looks good!').comments, 'Looks good!')

    def test_get_design_reviews(self):
        response = self.client.get(self.design_review_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # One design review exists

    def test_update_design_review(self):
        update_data = {
            'reviewer': 'Jane Doe',
            'comments': 'Updated review'
        }
        response = self.client.put(reverse('design_review-detail', args=[self.design_review.id]), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.design_review.refresh_from_db()
        self.assertEqual(self.design_review.reviewer, 'Jane Doe')
        self.assertEqual(self.design_review.comments, 'Updated review')

    def test_delete_design_review(self):
        response = self.client.delete(reverse('design_review-detail', args=[self.design_review.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(DesignReview.objects.count(), 0)  # Design review should be deleted