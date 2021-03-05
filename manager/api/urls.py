from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    # sells report urls
    path('list-create-sells',views.SellsListCreate.as_view(),name="sells-list"),
    path('sells-detail/<str:pk>',views.SellsReportDetail.as_view(),name="sells-detail"),

    # income expense 
    path('income-expenses',views.ExpensesIncomeList.as_view(),name="income-expenses"),
    path('income-expense-detail/<str:pk>',views.ExpensesIncomeDetail.as_view(),name="income-expense-detail"),

    # size 
    path('size',views.SizeList.as_view(),name="size-list"),
    path('size/<str:pk>',views.SizeDetail.as_view(),name="size-detail"),

    # amount paid 
    path('payments',views.SizeList.as_view(),name="payment-list"),
    path('payment/<str:pk>',views.SizeDetail.as_view(),name="payment-detail"),
]