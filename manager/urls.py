from django.urls import path, include

from . import views

app_name = "manager"

urlpatterns = [
    path('', views.index, name="index"),
    # api json
    path('api/',include("manager.api.urls")),


    path('add-sells', views.add_sells, name="add-sells"),
    path('add-sizes/<pk>', views.add_size, name="add-sizes"),
    path('manage-payments/<pk>', views.manage_payments, name="manage-payments"),

    path('sells-list', views.list_sells, name="sells-list"),
    path('sells-report-detail/<pk>', views.sells_report_detail, name="sells-report"),

    path('income-expense', views.add_income_expenses, name="income-expense"),
    path('money-list', views.list_money, name="money-list"),
    path('money-detail/<pk>', views.money_detail, name="money-detail"),

    path('get_income_expense', views.get_income_data, name="get_income_expense"),
    path('get_sells_data', views.get_sells_data, name="get_sells_data"),
]