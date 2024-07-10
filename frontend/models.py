from django.db import models # type: ignore
from simple_history.models import HistoricalRecords # type: ignore
from datetime import date

#Modele 

class Beneficiary(models.Model): #model dla beneficjenta programu socjalnego
    """"Model dla beneficjenta gruszy"""
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    place = models.CharField(max_length=100)
    bank_account_number = models.CharField(max_length=26)
    is_alive = models.BooleanField(default=True)
    version = models.PositiveIntegerField(default=0)
    history = HistoricalRecords()
    birth_date = models.DateField(default=date(2000,3,24))
    phone_num = models.IntegerField(default=123456789)
    place_of_residence = models.CharField(max_length=150, default='Brak Danych')

    def __str__(self): 
        return f"{self.first_name} - {self.last_name} - {self.place}" #zwrot f stringa 
    
class PaymentList(models.Model): #model dla listy wypłat
    name = models.CharField(max_length=150) #nazwa listy wypłat
    date_added = models.DateField(auto_now_add=True)
    Beneficiaries = models.ManyToManyField(Beneficiary, related_name='payments', through='PaymentListBeneficiary') #Zaciągnięcie danych z modelu beneficjenta

    def __str__(self):
        return f"{self.name} z dnia {self.date_added}"
    
class PaymentListBeneficiary(models.Model):
    payment_list = models.ForeignKey(PaymentList, on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('payment_list', 'beneficiary')

    def __str__(self):
        return f"{self.beneficiary} - {self.amount} on {self.payment_list}"
    
class PaymentHistory(models.Model): #model dla historii płatności 
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    payment_list = models.ForeignKey(PaymentList, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.beneficiary} - {self.payment_list} - {self.amount} - {self.date_added}"
    
class Benefit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Application(models.Model):
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    benefit = models.ForeignKey(Benefit, on_delete=models.CASCADE)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)
    household_type = models.CharField(max_length=20, choices=[('single', 'Jednoosobowe'), ('multiple', 'Wieloosobowe')])
    date_submitted = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)  # Dodajemy pole na wysokość świadczenia

    def save(self, *args, **kwargs):
        if self.benefit.name == "Grusza":
            self.amount = self.calculate_grusza_amount()
        super().save(*args, **kwargs)

    def calculate_grusza_amount(self):
        if self.household_type == 'one_person':
            if self.monthly_income <= 2001:
                return 1000
            elif self.monthly_income <= 2500:
                return 950
            elif self.monthly_income <= 3000:
                return 900
            else:
                return 850
        else:
            if self.monthly_income <= 2001:
                return 950
            elif self.monthly_income <= 2500:
                return 900
            elif self.monthly_income <= 3000:
                return 850
            else:
                return 800

    def __str__(self):
        return f"{self.beneficiary} - {self.benefit} - {self.amount}"

class ApplicationList(models.Model):
    benefit = models.ForeignKey(Benefit, on_delete=models.CASCADE)
    year = models.IntegerField()
    applications = models.ManyToManyField(Application, related_name='application_lists')

    def __str__(self):
        return f"{self.benefit.name} {self.year}"