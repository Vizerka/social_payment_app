from django.contrib import admin # type: ignore # type: ignore
from .models import Beneficiary, PaymentList, PaymentHistory, PaymentListBeneficiary
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(PaymentList)
admin.site.register(PaymentHistory)
admin.site.register(Beneficiary, SimpleHistoryAdmin)

# Register your models here.
