from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    phone=models.CharField(max_length=20,unique=True)
    
class Expense(models.Model):
    
    title=models.CharField(max_length=200)
    
    created_date=models.DateTimeField(auto_now=True)
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    EXPENSE_CATEGORIES = (
    (None,'Select'),
    ('Housing', 'Housing'),
    ('Transportation', 'Transportation'),
    ('Food', 'Food'),
    ('Healthcare', 'Healthcare'),
    ('Education', 'Education'),
    ('Entertainment', 'Entertainment'),
    ('Personal Care', 'Personal Care'),
    ('Debt Payments', 'Debt Payments'),
    ('Savings & Investments', 'Savings & Investments'),
    ('Gifts & Donations', 'Gifts & Donations'),
    ('Insurance', 'Insurance'),
    ('Travel', 'Travel'),
    ('Miscellaneous', 'Miscellaneous'),
)
    
    category = models.CharField(max_length=100,choices=EXPENSE_CATEGORIES,default="Select")
    
    payment_choice=(
        (None,'Select'),
        ('UPI','UPI'),
        ('Card','Card'),
        ('Cash','Cash')
    )
    
    payment_method= models.CharField(max_length=100,choices=payment_choice,default="Select")
    
    expense_date=models.DateField()
    
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.title
    