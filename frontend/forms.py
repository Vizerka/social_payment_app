from django import forms # type: ignore
from .models import Beneficiary, PaymentList, PaymentListBeneficiary
from django_select2.forms import Select2MultipleWidget, Select2Widget # type: ignore

class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = ['first_name', 'last_name', 'place', 'bank_account_number', 'payment_year', 'is_alive']
        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'place': 'Placówka',
            'bank_account_number': 'Nr rachunku bankowego',
            'payment_year': 'Rok wypłaty',
            'is_alive': 'Czy żyje',
        }

class PaymentListForm(forms.ModelForm):
    class Meta:
        model = PaymentList
        fields = ['name']
        labels = {'name': 'Nazwa Listy Wypłat'}

class PaymentListBeneficiaryForm(forms.ModelForm):
    beneficiary = forms.ModelChoiceField(queryset=Beneficiary.objects.filter(is_alive=True), widget=Select2Widget(attrs={'data-minimum-input-length': 0}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = PaymentListBeneficiary
        fields = ['beneficiary', 'amount']
        labels = {'amount': 'Kwota'}

class NewBeneficiaryForm(forms.ModelForm):
     class Meta:
          model = Beneficiary
          fields = ['first_name', 'last_name', 'place', 'bank_account_number', 'payment_year']
          labels = {'first_name': 'Imię',
                    'last_name': 'Nazwisko', 
                    'place': 'Placówka', 
                    'bank_account_number':'Nr Konta Bankowego', 
                    'payment_year':'Rok Wpłaty'
                    }
          widgets = {'first_name': forms.TextInput(),
                     'last_name': forms.TextInput(),
                     'place':  forms.TextInput(),
                     'bank_account_number': forms.TextInput(),
                     'payment_year':  forms.NumberInput(attrs={"min":2022, "max":2024,}),
                     }

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Wybierz plik Excel')