from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.forms import inlineformset_factory, NumberInput
from django.contrib.auth.decorators import login_required

from rest_framework.generics import GenericAPIView

from .models import (
    SellsReport,
    Size,
    PaidAmount,
    ExpensesIncomeModel,
)
from .forms import (
    SellsReportModelForm,
    SellsReportDetailForm,
    ExpensesIncomeModelForm
)

from .permission import check_if_admin

from .filters import SellsReportFilter, MoneyFilter

# @login_required(login_url="accounts:login")
# @check_if_admin
def index(request):
    sells_qs = SellsReport.get_current_month.all().order_by('-date')[:3]
    expenses_income_qs = ExpensesIncomeModel.get_current_month.all()
    
    income = 0
    expense = 0
    
    if expenses_income_qs:
        for field in expenses_income_qs:
            if field.is_income:
                income = income + field.price
            else:
                expense = expense + field.price
    profit = income - expense

    return render(request,"manager/index.html",{
        "sells_qs":sells_qs,
        "income":income,
        "expense":expense,
        "profit":profit,
        "expenses_income_qs":expenses_income_qs,
    })

# @login_required(login_url="accounts:login")
# @check_if_admin
def add_sells(request):
    if request.method == 'GET':
        forms = SellsReportModelForm()
        return render(request, "manager/add-sells.html",{
            "form":forms,
        })

    if request.method == 'POST':
        forms = SellsReportModelForm(request.POST or None)
        if forms.is_valid():
            instances = forms.save()
            return HttpResponseRedirect(reverse("manager:add-sizes",args=[str(instances.pk)]))
        else:
            return render(request, "manager/add-sells.html",{
                "form":forms,
            })           

# @login_required(login_url="accounts:login")
# @check_if_admin
def add_size(request,pk):
    qs = get_object_or_404(SellsReport,pk=pk)

    SellsReportModelFormset = inlineformset_factory(SellsReport, Size,widgets={
        "size":NumberInput(
            attrs={
                "class":"form-control",
            }
        ),
        "price":NumberInput(
            attrs={
                "class":"form-control",
            }
        ),
        "quantity":NumberInput(
            attrs={
                "class":"form-control",
            }
        ),
    }, fields='__all__')

    if request.method == 'GET':
        formset = SellsReportModelFormset(instance=qs)
        return render(request, "manager/add-size.html",{
            "form":formset,
            "qs":qs,
        })

    if request.method == 'POST':
        formset = SellsReportModelFormset(request.POST, instance=qs)
        if formset.is_valid():
            formset.save()
            # to cal total_price
            total_price = 0
            size_qs = Size.objects.filter(item_sold=qs).distinct()
            for x in size_qs:
                total_price = total_price + (x.price * x.quantity)
            total_price = total_price + (total_price * qs.tax * 0.01)
            qs.total_price = total_price
            qs.balance = total_price
            qs.save()

            if request.POST.get("add_payment"):
                return HttpResponseRedirect(reverse("manager:manage-payments",args=[str(qs.pk)]))
            if request.POST.get("view"):
                return HttpResponseRedirect(reverse("manager:sells-report",args=[str(qs.pk)]))


        return render(request, "manager/add-size.html",{
            "form":formset,
            "qs":qs,
        })

# @login_required(login_url="accounts:login")
# @check_if_admin
def manage_payments(request,pk):
    qs = get_object_or_404(SellsReport,pk=pk)

    SellsReportModelFormset = inlineformset_factory(SellsReport, PaidAmount,widgets={
        "amount_paid":NumberInput(attrs={
            "class":"form-control",
        }),
    }, fields='__all__')

    if request.method == 'GET':
        formset = SellsReportModelFormset(instance=qs)
        return render(request, "manager/payments.html",{
            "form":formset,
            "qs":qs,
        })

    if request.method == 'POST':
        formset = SellsReportModelFormset(request.POST, instance=qs)
        if formset.is_valid():
            formset.save()
            # to cal paid amount
            amount_paid = 0
            instance = PaidAmount.objects.filter(item_sold=qs).distinct()
            for x in instance:
                amount_paid = amount_paid + x.amount_paid
            
            qs.balance = qs.total_price - amount_paid
            if qs.balance == 0:
                qs.payment_completed = True
            qs.save()
            return HttpResponseRedirect(reverse("manager:sells-report",args=[str(qs.pk)]))

        return render(request, "manager/payments.html",{
            "form":formset,
            "qs":qs,
        })


# @login_required(login_url="accounts:login")
# @check_if_admin
def add_income_expenses(request):
    if request.method == 'GET':
        form = ExpensesIncomeModelForm()
        return render(request,"manager/income.html",{
            "form":form,
        })

    if request.method == 'POST':
        form = ExpensesIncomeModelForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            if request.POST.get('add_another'):
                return HttpResponseRedirect(reverse("manager:income-expense"))
            if request.POST.get("add"):
                return HttpResponseRedirect(reverse("manager:money-list"))
            if request.POST.get("add_and_view"):
                return HttpResponseRedirect(reverse("manager:money-detail",args=[str(obj.pk)]))

        else:
            return render(request,"manager/income.html",{
                "form":form,
            })


# @login_required(login_url="accounts:login")
# @check_if_admin
def list_sells(request):
    qs = SellsReport.objects.all().order_by("-date")

    sells_filter = SellsReportFilter(request.GET, queryset=qs)
    qs = sells_filter.qs

    paginator = Paginator(qs, 15)

    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    return render(request,"manager/list-sells.html",{
        "qs":qs,
        "qs_filter":sells_filter,
    })

# @login_required(login_url="accounts:login")
# @check_if_admin
def sells_report_detail(request,pk):
    qs = get_object_or_404(SellsReport,pk=pk)

    if request.method == 'GET':
        form = SellsReportDetailForm(instance=qs)

        return render(request,"manager/sells-detail.html",{
            "qs":qs,
            "form":form,
        })
    if request.method == 'POST':
        form = SellsReportDetailForm(request.POST or None,instance=qs)
        if form.is_valid():
            form.save()

            if request.POST.get("save"):
                return HttpResponseRedirect(reverse("manager:sells-report",args=[str(pk)]))
            if request.POST.get("save_and_add_size"):
                return HttpResponseRedirect(reverse("manager:add-sizes",args=[str(pk)]))
            if request.POST.get("save_and_add_payment"):
                return HttpResponseRedirect(reverse("manager:manage-payments",args=[str(pk)]))

        return render(request,"manager/sells-detail.html",{
            "qs":qs,
            "form":form,
        })

# @login_required(login_url="accounts:login")
# @check_if_admin
def list_money(request):
    qs = ExpensesIncomeModel.objects.all().order_by("-date")

    qs_filter = MoneyFilter(request.GET, queryset=qs)
    qs = qs_filter.qs

    paginator = Paginator(qs, 15)

    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    return render(request,"manager/list-money.html",{
        "qs":qs,
        "qs_filter":qs_filter,
    })

# @login_required(login_url="accounts:login")
# @check_if_admin
def money_detail(request,pk):
    qs = get_object_or_404(ExpensesIncomeModel, pk=pk)

    if request.method == 'GET':
        form = ExpensesIncomeModelForm(instance=qs)
        return render(request,"manager/money-detail.html",{
            "qs":qs,
            "form":form,
        })

    if request.method == 'POST':
        form = ExpensesIncomeModelForm(request.POST or None, instance=qs)
        if form.is_valid():
            form.save()

            if request.POST.get("save_and_cont"):
                return HttpResponseRedirect(reverse("manager:money-detail",args=[str(qs.pk)]))
            if request.POST.get("save"):
                return HttpResponseRedirect(reverse("manager:money-list"))
            if request.POST.get("save_and_add_another"):
                return HttpResponseRedirect(reverse("manager:income-expense"))
            
        else:
            return render(request,"manager/money-detail.html",{
            "qs":qs,
            "form":form,
            })

# @login_required(login_url="accounts:login")
# @check_if_admin
def get_income_data(request):
    qs = ExpensesIncomeModel.get_current_month.all()
    previous_qs = qs.first()

    dates = []
    expense = []
    income = []

    for x in qs.order_by('date'):
        if previous_qs.date == x.date and expense and income:
            if x.is_income:
                # to get income
                income_array_len = len(income)
                income[income_array_len-1] = income[income_array_len-1] + round(x.price/1000,2)
            else:
                # to get expense
                expense_array_len = len(expense)
                expense[expense_array_len-1] = expense[expense_array_len-1] + round(x.price/1000,2)

        else:
            dates.append(x.date.strftime("%d-%m-%Y"))
            if x.is_income:
                income.append(round(x.price/1000,2))
                expense.append(0)
            else:
                income.append(0)
                expense.append(round(x.price/1000,2))
        previous_qs = x
    
    return JsonResponse({
        "dates":dates,
        "expense":expense,
        "income":income,
    },status=200)

# @login_required(login_url="accounts:login")
# @check_if_admin
def get_sells_data(request):
    qs = SellsReport.get_current_month.all()
    previous_qs = qs.first()

    dates = []
    sells = []

    for x in qs.order_by('date'):
        if previous_qs.date == x.date and sells:
            sells_len = len(sells)
            sells[sells_len-1] = sells[sells_len-1] + round(x.total_price/10000,2)
        else:
            dates.append(x.date.strftime("%d-%m-%Y"))
            sells.append(round(x.total_price/10000,2))
            
        previous_qs = x

    return JsonResponse({
        "dates":dates,
        "sells":sells,
    },status=200)