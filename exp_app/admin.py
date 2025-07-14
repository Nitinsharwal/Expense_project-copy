from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_title = "Expense Tracker"
admin.site.site_header = "Expense Tracker || Admin - Chetan Sharwal"
admin.site.url = "Expense Tracker"
admin.site.register(current_ammount)

class TrackingAdmin(admin.ModelAdmin):
    list_display = ['current_balance',
    'expense_type',
    'ammount',
    'description',
    'created_at'
    ]
    search_fields = ['expense_type','description']
    ordering = ['-created_at']
    list_filter = ['expense_type']

admin.site.register(Tracker,TrackingAdmin)