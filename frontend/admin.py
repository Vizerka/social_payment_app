from django.contrib import admin # type: ignore # type: ignore
from .models import Beneficiary, PaymentList, PaymentHistory

admin.site.register(Beneficiary)
admin.site.register(PaymentList)
admin.site.register(PaymentHistory)

# Register your models here.
