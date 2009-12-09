from django.contrib import admin
from django_freshbooks.models import *

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category,CategoryAdmin)

class ClientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Client,ClientAdmin)

class EstimateAdmin(admin.ModelAdmin):
    pass
admin.site.register(Estimate,EstimateAdmin)

class ExpenseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Expense,ExpenseAdmin)

class InvoiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Invoice,InvoiceAdmin)

class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item,ItemAdmin)

class PaymentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Payment,PaymentAdmin)

class ProjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Project,ProjectAdmin)

class RecurringAdmin(admin.ModelAdmin):
    pass
admin.site.register(Recurring,RecurringAdmin)

class StaffAdmin(admin.ModelAdmin):
    pass
admin.site.register(Staff,StaffAdmin)

class TaskAdmin(admin.ModelAdmin):
    pass
admin.site.register(Task,TaskAdmin)

class TimeEntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(TimeEntry,TimeEntryAdmin)
