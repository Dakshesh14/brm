import django_filters
from django.db import models
from django import forms

from .models import SellsReport, ExpensesIncomeModel

class SellsReportFilter(django_filters.FilterSet):
    amount_start = django_filters.NumberFilter(field_name="total_price",lookup_expr="gte")
    amount_end = django_filters.NumberFilter(field_name="total_price",lookup_expr="lte")
    class Meta:
        model = SellsReport
        fields = [
            'client',
            'payment_completed',
        ]


class MoneyFilter(django_filters.FilterSet):
    class Meta:
        model = ExpensesIncomeModel
        fields = '__all__'
        exclude = [
            'date',
        ]