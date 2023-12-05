from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import WishlistItem

@receiver(post_save, sender=WishlistItem)
def wishlist_item_created(sender, instance, created, **kwargs):
    """
    Signal handler for when a WishlistItem is created.
    """
    if created:
        print(f"Wishlist item created: {instance.product.name}")

@receiver(post_delete, sender=WishlistItem)
def wishlist_item_deleted(sender, instance, **kwargs):
    """
    Signal handler for when a WishlistItem is deleted.
    """
    print(f"Wishlist item deleted: {instance.product.name}")
