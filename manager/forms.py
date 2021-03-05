from django import forms

from .models import SellsReport, ExpensesIncomeModel

class SellsReportModelForm(forms.ModelForm):
    class Meta:
        model = SellsReport
        fields = [
            'client',
            'client_phone',
            'tax',
            'date'
        ]
    
    client = forms.CharField(
        label="Client's name",
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "max_length":255,
            "placeholder":"Batman",
        })
    )
    client_phone = forms.CharField(
        label="Client's phone number",
        required=False,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Add Client Phone Number",
        })
    )
    tax = forms.FloatField(
        label="Tax",
        widget=forms.NumberInput(attrs={
            "class":"form-control",
            "placeholder": "Enter tax(in %)",
        })
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            "class":"form-control",
        })
    )

class SellsReportDetailForm(forms.ModelForm):
    client = forms.CharField(
        label="Client's name",
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "max_length":255,
            "placeholder":"Batman",
        })
    )
    client_phone = forms.CharField(
        label="Client's phone number",
        required=False,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Not Been Added",
        })
    )
    tax = forms.FloatField(
        label="Tax",
        widget=forms.NumberInput(attrs={
            "class":"form-control",
            "placeholder": "Enter tax(in %)",
        })
    )    
    total_price = forms.FloatField(
        label="Total",
        widget=forms.NumberInput(attrs={
            "class":"form-control",
            "placeholder": "Enter tax(in %)",
        })
    )    
    balance = forms.FloatField(
        label="Balance",
        widget=forms.NumberInput(attrs={
            "class":"form-control",
            "placeholder": "Enter tax(in %)",
        })
    )    
    payment_completed = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class":"form-check-input",
        })
    )
    date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            "class":"form-control",
        })
    )
    class Meta:
        model = SellsReport
        fields = '__all__'



class ExpensesIncomeModelForm(forms.ModelForm):
    class Meta:
        model = ExpensesIncomeModel
        fields = '__all__'

        widgets = {
            "description": forms.TextInput(attrs={
                "class":"form-control",
            }),
            "price": forms.NumberInput(attrs={
                "class":"form-control",
            }),
            "is_income": forms.CheckboxInput(attrs={
                "class":"form-check-input",
            }),
        }
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            "class":"form-control",
        })
    )