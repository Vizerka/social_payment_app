from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .models import Beneficiary, PaymentList, PaymentHistory, PaymentListBeneficiary
from .forms import BeneficiaryForm, PaymentListForm, NewBeneficiaryForm, PaymentListBeneficiaryForm
from django.db.models import Q
from django.core.paginator import Paginator  # Import Paginator
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError

def index(request): #zdefiniowanie strony index
    return render(request, 'frontend/index.html')
def logout(request):
    return render(request, 'frontend/logout.html')

@login_required
def beneficiary_list(request): #zdefiniowanie strony z listą beneficjentów 
    #funkcja dla wyszukiwania beneficjentów po Imieniu lub Nazwisku lub Placówce
    query = request.GET.get('Q') 
    if query: 
        beneficiaries = Beneficiary.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(place__icontains=query)
        )
        paginator = Paginator(beneficiaries, 5)  # 50 wpisów na stronę
        page_number = request.GET.get('page')
    else:
        #w przypadku braku podania danych w formularzu zostanie wyświetlona pełna baza
        beneficiaries = Beneficiary.objects.all()
    # Paginacja
    paginator = Paginator(beneficiaries, 5)  # 50 wpisów na stronę
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'frontend/beneficiary_list.html', {'beneficiaries':beneficiaries, 'page_obj': page_obj})

@login_required
def beneficiary_add(request): #zdefiniowanie manualnego dodawania użytkowników 
    if request.method != 'POST':
        form = NewBeneficiaryForm()
    else:
        form = NewBeneficiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frontend:beneficiary_add')
    return render(request, 'frontend/beneficiary_add.html', {'form':form})

@login_required
def beneficiary_detail(request, pk):
    beneficiary = get_object_or_404(Beneficiary, pk=pk)
    payment_history = PaymentHistory.objects.filter(beneficiary=beneficiary)
    return render(request, 'frontend/beneficiary_detail.html', {'beneficiary': beneficiary, 'payment_history': payment_history})



@login_required
#def payment_add(request):
#    if request.method == 'POST':
#        form = PaymentListForm(request.POST)
#        if form.is_valid():
#            payment_add = form.save()
#            for beneficiary in form.cleaned_data['Beneficiaries']:
#                PaymentHistory.objects.create(beneficiary=beneficiary, payment_add=payment_add)
#            return redirect('frontend:payment_add')
#    else:
#        form = PaymentListForm()
#    return render(request, 'frontend/payment_add.html', {'form': form})
def payment_add(request):
    if request.method == 'POST':
        form = PaymentListForm(request.POST)
        if form.is_valid():
            payment_list = form.save()
            return redirect('frontend:payment_add_beneficiary', pk=payment_list.pk)
    else:
        form = PaymentListForm()
    return render(request, 'frontend/payment_add.html', {'form': form})

@login_required
def payment_add_beneficiary(request, pk):
    payment_list = PaymentList.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = PaymentListBeneficiaryForm(request.POST)
        if form.is_valid():
            payment_beneficiary = form.save(commit=False)
            payment_beneficiary.payment_list = payment_list  # Przypisanie payment_list tutaj
            try:
                if PaymentListBeneficiary.objects.filter(payment_list=payment_list, beneficiary=payment_beneficiary.beneficiary).exists():
                    form.add_error('beneficiary', 'Ten beneficjent już istnieje na tej liście wypłat.')
                else:
                    payment_beneficiary.save()

                    PaymentHistory.objects.create(
                        beneficiary=payment_beneficiary.beneficiary,
                        payment_list=payment_list,
                        amount=payment_beneficiary.amount
                    )

                    return redirect('frontend:payment_add_beneficiary', pk=payment_list.pk)
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = PaymentListBeneficiaryForm()
    
    return render(request, 'frontend/payment_add_beneficiary.html', {'form': form, 'payment_list': payment_list})

@login_required
def payment_detail(request, pk):
    payment = get_object_or_404(PaymentList, pk=pk)
    payment_list_beneficiaries = PaymentListBeneficiary.objects.filter(payment_list=payment)
    
    beneficiaries = [
        {
            "first_name": plb.beneficiary.first_name,
            "last_name": plb.beneficiary.last_name,
            "place": plb.beneficiary.place,
            "amount": plb.amount
        }
        for plb in payment_list_beneficiaries
    ]
    
    return render(request, 'frontend/payment_detail.html', {'payment': payment, 'beneficiaries': beneficiaries})

@login_required
def payment_list(request):
    payments = PaymentList.objects.all()
    return render(request, 'frontend/payment_list.html', {'payments': payments})



# Create your views here.
