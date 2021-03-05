import datetime # for querying monthly model

from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class get_current_month_data(models.Manager):
    def get_queryset(self):
        today = datetime.date.today()
        return super().get_queryset().filter(date__month=today.month)


# model to manage all the expense 
class ExpensesIncomeModel(models.Model):
    description = models.CharField(max_length=450)
    price = models.FloatField()

    is_income = models.BooleanField(default=False)

    date = models.DateField()

    objects = models.Manager()
    get_current_month = get_current_month_data()

    def __str__(self):
        return f"{self.description} - {self.price}"

# the main products sold manager
class SellsReport(models.Model):
    # client info
    client = models.CharField(max_length=255) 
    client_phone = PhoneNumberField(null=True, blank=True)

    # price
    tax = models.IntegerField()
    total_price = models.FloatField(default=2000000)
    balance = models.FloatField(default=2000000)

    payment_completed = models.BooleanField(default=False)

    date = models.DateField()

    objects = models.Manager()
    get_current_month = get_current_month_data()

    def __str__(self):
        return self.client
    

# to add to main item sold manager
class Size(models.Model):
    size = models.IntegerField()
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    item_sold = models.ForeignKey('SellsReport',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.size} - {self.price}"


# to add to main item sold manager
class PaidAmount(models.Model):
    amount_paid = models.FloatField()
    date = models.DateField(auto_now_add=True)
    item_sold = models.ForeignKey('SellsReport',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.amount_paid} on {self.date}"