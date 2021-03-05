from django.contrib import admin

# from .models import ExpensesIncomeModel, Size, PaidAmount, SellsReport

# class InLineSizeItemSold(admin.TabularInline):
#     model = Size

# class InLinePaidAmountItemSold(admin.TabularInline):
#     model = PaidAmount


# class SellsReportAdmin(admin.ModelAdmin):
#     inlines = [InLineSizeItemSold,InLinePaidAmountItemSold]
#     list_display = ('client','balance','payment_completed',)
#     list_per_page = 15
#     search_fields = ('client',)
#     list_filter = ('payment_completed',)
#     # readonly_fields = ('date',)

# class PaidAmountAdmin(admin.ModelAdmin):
#     readonly_fields = ('date',)

# class ExpensesIncomeModelAdmin(admin.ModelAdmin):
#     readonly_fields = ('date',)

# admin.site.register(SellsReport,SellsReportAdmin)
# admin.site.register(Size)
# admin.site.register(ExpensesIncomeModel,ExpensesIncomeModelAdmin)
# admin.site.register(PaidAmount,PaidAmountAdmin)