from django.contrib import admin
from .models import Budget, Transaction, Account, TransactionCategory, TransactionTag

# Register your models here.

class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 0

class BudgetAdmin(admin.ModelAdmin):
    inlines = [TransactionInline]
    list_display = ('name',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'account', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at', 'account')

class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at', 'updated_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)



admin.site.register(Account, AccountAdmin)
admin.site.register(TransactionCategory, CategoryAdmin)
admin.site.register(TransactionTag, TagAdmin)
admin.site.register(Budget, BudgetAdmin)
