from django import forms
from expense.models import User,Expense
from django.contrib.auth.forms import UserCreationForm




class SignUpForm(UserCreationForm):
    password1=forms.PasswordInput(attrs={"class":"from-control"})
    password2=forms.PasswordInput(attrs={"class":"from-control"})
    class Meta:
        
        model=User
        
        fields=["username","email","phone","password1","password2"]
        
        
class SignInForm(forms.Form):
    
    
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    
class ExpenseForm(forms.ModelForm):
    
    
    class Meta:
       
        model=Expense
        
        fields=["title","amount","category","expense_date"]