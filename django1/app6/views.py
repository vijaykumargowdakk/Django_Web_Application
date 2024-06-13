from django.shortcuts import render
from django.db import IntegrityError
from .models import Customer, SavingsAccount
from .forms import CustomerForm, SavingsAccountForm

def index(request):
    customer_form = CustomerForm()
    savings_form = SavingsAccountForm()
    success_message = None
    error_message = None 

    if request.method == 'POST':
        if 'registration' in request.POST:
            customer_form = CustomerForm(request.POST)
            if customer_form.is_valid():
                try:  
                    customer = customer_form.save()
                    success_message = f"Customer {customer.customer_id} registered successfully!"
                    customer_form = CustomerForm()  
                except IntegrityError:
                    error_message = "Customer with this Aadhaar number already exists."

        elif 'savings_account' in request.POST:
            customer_id = request.POST['customer_id']
            try:
                customer = Customer.objects.get(customer_id=customer_id)  # Ensure customer exists
                savings_form = SavingsAccountForm(request.POST)
                if savings_form.is_valid():
                    account = savings_form.save(commit=False)
                    account.customer = customer
                    account.save()
                    success_message = f"Savings Account opened for customer {customer_id}!"
                    savings_form = SavingsAccountForm()  
                else:
                    error_message = "Invalid input for Savings Account."
            except Customer.DoesNotExist:
                error_message = "Customer ID does not exist."


    return render(request, 'app6/index.html', {
        'customer_form': customer_form,
        'savings_form': savings_form,
        'customer_id': request.POST.get('customer_id'),
        'success_message': success_message,
        'error_message': error_message
    })
