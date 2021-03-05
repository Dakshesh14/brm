from rest_framework import serializers

from manager.models import (
    SellsReport,
    Size,
    PaidAmount,
    ExpensesIncomeModel,
)

class SellsReportListSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="manager:api:sells-detail",
        lookup_field="pk",
    )
    class Meta:
        model = SellsReport
        fields = [
            'client',
            'client_phone',
            'balance',
            'payment_completed',
            'detail_url',
        ]


class SellsReportDetailSerializer(serializers.ModelSerializer):
    date_time = serializers.DateTimeField(format="%H:%M %d-%m-%Y",read_only=True)
    class Meta:
        model = SellsReport
        fields = [
            'client',
            'client_phone',
            'tax',
            'date_time',
            'total_price',
            'balance',
            'payment_completed',
        ]

class SizeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class PaidAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaidAmount
        fields = '__all__'

class ExpensesIncomeSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%m-%Y",read_only=True)
    class Meta:
        model = ExpensesIncomeModel
        fields = '__all__'
