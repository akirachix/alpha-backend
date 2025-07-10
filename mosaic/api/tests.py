import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date
from payment.models import Payment
from decimal import Decimal


def api_client():
    return APIClient()

def sample_payment():
    return Payment.objects.create(
        amount=Decimal("1000.00"),
        phone_number="0700000000",
        mpesa_receipt_number="MP123456789",
        paid_at=date.today()
    )


class TestPaymentAPI:
    def test_create_payment(self, api_client):
        url = reverse("payment-list")
        data = {
            "amount": "1500.00",
            "phone_number": "0711223344",
            "mpesa_receipt_number": "MP987654321",
            "paid_at": date.today().isoformat()
        }
        response = api_client.post(url, data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["amount"] == "1500.00"
        
    def test_read_payment(self, api_client, sample_payment):
        url = reverse("payment-detail", args=[sample_payment.id])
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["phone_number"] == sample_payment.phone_number

    def test_update_payment(self, api_client, sample_payment):
        url = reverse("payment-detail", args=[sample_payment.id])
        updated_data = {
            "amount": "2000.00",
            "phone_number": sample_payment.phone_number,
            "mpesa_receipt_number": sample_payment.mpesa_receipt_number,
            "paid_at": sample_payment.paid_at.isoformat()
        }
        response = api_client.put(url, updated_data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["amount"] == "2000.00"

    def test_delete_payment(self, api_client, sample_payment):
        url = reverse("payment-detail", args=[sample_payment.id])
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Payment.objects.filter(id=sample_payment.id).exists()

