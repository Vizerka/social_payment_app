from django.db import models # type: ignore
from simple_history.models import HistoricalRecords # type: ignore

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