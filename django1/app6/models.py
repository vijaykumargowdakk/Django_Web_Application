from django.db import models

class Customer(models.Model):
    customer_id = models.CharField(max_length=10, unique=True, default="CID_5001")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    aadhaar = models.CharField(max_length=15, unique=True)
    pincode = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if it's a new customer (no primary key yet)
            last_customer = Customer.objects.order_by('-id').first()
            if last_customer:
                last_id = int(last_customer.customer_id.split('_')[1])
                self.customer_id = f"CID_{last_id + 1}"
            else:  # No previous customers exist
                self.customer_id = "CID_5001"  # Start from the initial value
        super().save(*args, **kwargs)

class SavingsAccount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    initial_amount = models.DecimalField(max_digits=10, decimal_places=2)

