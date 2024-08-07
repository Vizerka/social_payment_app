from django.urls import path  # type: ignore

from . import views

app_name = 'frontend'
urlpatterns = [
    path('', views.index, name='index'),
    path('beneficiary_list', views.beneficiary_list, name='beneficiary_list'),
    path('beneficiary/<int:pk>/', views.beneficiary_detail, name='beneficiary_detail'),
    path('beneficiary/<int:pk>/edit/', views.beneficiary_edit, name='beneficiary_edit'),
    path('payment_add/', views.payment_add, name='payment_add'),
    path('payment_add/<int:pk>/beneficiary/', views.payment_add_beneficiary, name='payment_add_beneficiary'),
    path('beneficiary/add/', views.beneficiary_add, name='beneficiary_add'),
    path('payment_list_all', views.payment_list, name='payment_list_all'),
    path('payment_detail/<int:pk>/', views.payment_detail, name='payment_detail'),
    path('export_payment_list_to_excel/<int:pk>/', views.export_payment_list_to_excel, name='export_payment_list_to_excel'),
    path('import_beneficiaries/', views.import_beneficiaries, name='import_beneficiaries'),
    path('beneficiary_list_full', views.beneficiary_list_full, name='beneficiary_list_full'),
    path('application/create/', views.application_create, name='application_create'),
    path('application/list/', views.application_list_all, name='application_list_all'),
    path('application/list/<int:benefit_id>/<int:year>/', views.application_list_detail, name='application_list_detail'),
   ]