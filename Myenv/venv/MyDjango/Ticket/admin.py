from django.contrib import admin
# Register your models here.
from .models import Account
from .forms import AdminAccountForm

class AccountAdmin(admin.ModelAdmin):
    list_display = ['__str__','email','timestamp','update']
    form = AdminAccountForm
    # class Meta:
    #     model = Account


admin.site.register(Account,AccountAdmin)
