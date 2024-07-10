from django.contrib import admin # type: ignore # type: ignore
from .models import Beneficiary, PaymentList, PaymentHistory, PaymentListBeneficiary, Benefit, ApplicationList, Application
from simple_history.admin import SimpleHistoryAdmin # type: ignore

admin.site.register(PaymentList)
admin.site.register(PaymentHistory)
admin.site.register(Beneficiary, SimpleHistoryAdmin)
admin.site.register(Benefit)
admin.site.register(ApplicationList)
admin.site.register(Application)

# Register your models here.
