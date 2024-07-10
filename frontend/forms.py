from django import forms # type: ignore
from .models import Beneficiary, PaymentList, PaymentListBeneficiary, Application, Benefit
from django_select2.forms import Select2MultipleWidget, Select2Widget # type: ignore
from django.forms import inlineformset_factory

class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = ['first_name', 'last_name', 'place', 'bank_account_number', 'is_alive', 'version']
        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'place': 'Placówka',
            'bank_account_number': 'Nr rachunku bankowego',
            'is_alive': 'Czy aktywny?',
        }
        widgets = {'version': forms.HiddenInput()}
    version = forms.IntegerField(widget=forms.HiddenInput())

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
          fields = ['first_name', 'last_name', 'place', 'bank_account_number',]
          labels = {'first_name': 'Imię',
                    'last_name': 'Nazwisko', 
                    'place': 'Placówka', 
                    'bank_account_number':'Nr Konta Bankowego', 
                    }
          widgets = {'first_name': forms.TextInput(),
                     'last_name': forms.TextInput(),
                     'place':  forms.TextInput(),
                     'bank_account_number': forms.TextInput(),
                     }

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Wybierz plik Excel')

class ApplicationForm(forms.ModelForm):
    beneficiary = forms.ModelChoiceField(queryset=Beneficiary.objects.filter(is_alive=True), widget=Select2Widget(attrs={'data-minimum-input-length': 0}))
    class Meta:
        model = Application
        fields = ['beneficiary', 'benefit', 'monthly_income', 'household_type']
        labels = {'beneficiary': 'beneficjent',
                  'benefit': 'Świadczenie',
                  'monthly_income': 'Średni dochód brutto na osobę z ostanich 3 miesięcy',
                  'household_type':'Typ gospodarstwa domowego:'}

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['benefit'].queryset = Benefit.objects.all()

class PaymentListBulkEditForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    beneficiaries = forms.ModelMultipleChoiceField(queryset=Beneficiary.objects.all())

class PaymentListBeneficiaryForm(forms.ModelForm):
    class Meta:
        model = PaymentListBeneficiary
        fields = ['beneficiary', 'amount']

PaymentListBeneficiaryFormSet = inlineformset_factory(
    PaymentList, PaymentListBeneficiary, form=PaymentListBeneficiaryForm, extra=0
)

class PaymentListBeneficiaryForm(forms.ModelForm):
    class Meta:
        model = PaymentListBeneficiary
        fields = ['beneficiary', 'amount']