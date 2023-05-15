from django.contrib import admin
from .models import Transaction, Account, TransactionCategory, TransactionTag

# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'account', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at', 'account')

class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at', 'updated_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
 

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(TransactionCategory, CategoryAdmin)
admin.site.register(TransactionTag, TagAdmin)
