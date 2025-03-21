from django.contrib import admin
from .models import Loan
# Register your models here.
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
  list_display = ['name', 'reason', 'amount', 'date', 'created']
  list_filter = ['date', 'amount']
  search_fields = ['name', 'amount']
  ordering = ['-date']
  list_editable = ['amount', 'date']
