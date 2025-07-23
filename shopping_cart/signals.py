from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Item

@receiver(post_save, sender=Item)
def update_order_total_on_save(sender, instance, **kwargs):
    instance.order.update_total_price()
@receiver(post_delete, sender=Item)
def update_order_total_on_delete(sender, instance, **kwargs):
    instance.order.update_total_price()