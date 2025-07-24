from django.test import TestCase
from .models import Design
from decimal import Decimal


class DesignModelTests(TestCase):
    def setUp(self):
        self.design = Design.objects.create(
            design_id="D001",
            design_name="Floral Dress",
            price=199.99,
            material_type="Cotton",
            design_image="floral.jpg",
            category="Dresses",
            design_size="Medium"
        )
    def test_create_design(self):
        design = Design.objects.create(
            design_id="D002",
            design_name="Striped Shirt",
            price=99.99,
            material_type="Linen",
            design_image="striped.jpg",
            category="Shirts",
            design_size="Large"
        )
        self.assertEqual(design.design_name, "Striped Shirt")
        self.assertEqual(design.price, 99.99)
    def test_retrieve_design(self):
        design = Design.objects.get(design_id="D001")
        self.assertEqual(design.design_name, "Floral Dress")
        self.assertEqual(design.material_type, "Cotton")
    def test_update_design(self):
        design = Design.objects.get(design_id="D001")
        design.price = Decimal("149.99")
        design.design_size = "Small"
        design.save()
        updated = Design.objects.get(design_id="D001")
        self.assertEqual(updated.price, Decimal("149.99"))
        self.assertEqual(updated.design_size, "Small")
    def test_delete_design(self):
        design = Design.objects.get(design_id="D001")
        design.delete()
        with self.assertRaises(Design.DoesNotExist):
            Design.objects.get(design_id="D001")












