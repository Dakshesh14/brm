# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver

# from .models import ItemSold, Size, PaidAmount

# @receiver(post_save, sender=ItemSold)
# def calculate_amount_and_balance(sender, instance, *args, **kwargs):
#     instance.calculate_amount_and_balance(save=False)


# # post_save.connect(calculate_amount_and_balance, sender=ItemSold)