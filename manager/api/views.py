from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import (
    SellsReportListSerializer,
    SellsReportDetailSerializer,
    ExpensesIncomeSerializer,
    SizeListSerializer,
    PaidAmountSerializer,
)

from manager.models import (
    ExpensesIncomeModel,
    SellsReport,
    Size,
    PaidAmount,
)

from .pagination import PostPageNumberPagination

class SellsListCreate(generics.ListCreateAPIView):
    queryset = SellsReport.objects.all()
    serializer_class = SellsReportListSerializer
    filter_backends = [SearchFilter,OrderingFilter,]
    search_fields = ['client',]
    ordering_fields = ['payment_completed','date_time',]
    pagination_class = PostPageNumberPagination


class SellsReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SellsReport.objects.all()
    serializer_class = SellsReportDetailSerializer
    lookup_field = 'pk'


class ExpensesIncomeList(generics.ListCreateAPIView):
    queryset = ExpensesIncomeModel.objects.all()
    serializer_class = ExpensesIncomeSerializer


class ExpensesIncomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExpensesIncomeModel.objects.all()
    serializer_class = ExpensesIncomeSerializer
    lookup_field = 'pk'


class SizeList(generics.ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeListSerializer


class SizeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeListSerializer
    lookup_field = 'pk'


class PaidAmountList(generics.ListCreateAPIView):
    queryset = PaidAmount.objects.all()
    serializer_class = PaidAmountSerializer


class PaidAmountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaidAmount.objects.all()
    serializer_class = PaidAmountSerializer
    lookup_field = 'pk'
