import django_tables2 as tables
from .models import PaymentListBeneficiary

class PaymentListBeneficiaryTable(tables.Table):
    edit = tables.TemplateColumn(template_name='frontend/payment_list_edit_column.html', orderable=False)

    class Meta:
        model = PaymentListBeneficiary
        fields = ('beneficiary', 'amount')
        attrs = {"class": "table table-striped table-bordered"}