from django.shortcuts import redirect, render
from django.views import View
from expense.models import Expense
from expense.forms import ExpenseForm, SignInForm, SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from expense.decorators import sigin_required
from django.views.decorators.cache import never_cache

decs=[sigin_required,never_cache]  
 # Create your views here.
class SignUpView(View):
    template_name="signup.html"
    
    form_class=SignUpForm
    
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data)
        
        if form_instance.is_valid():
            form_instance.save()
            
            print("created")
            
            return redirect("signup")            
            
       
        print("not created")
        return render(request,self.template_name,{"form":form_instance})
    
class SigninView(View):
    
    template_name="signin.html"
    
    form_class=SignInForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            uname=data.get("username")
            
            pwd=data.get("password")
            
            
            user_obj=authenticate(request,username=uname,password=pwd)
            if user_obj:
                login(request,user_obj)
                
                print("session started")
                
                return redirect("index")
        
        print("invalid credtinal")
        
        return render(request,self.template_name,{"form":form_instance})

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        
        logout(request)
        
        return redirect("signin")
    
@method_decorator(decs,name="dispatch")
class IndexView(View):
    template_name="index.html"
    
    form_class=ExpenseForm
    
    def get(self,request,*args,**kwargs):
        
        qs=Expense.objects.filter(owner=request.user)
        
        form_instance=self.form_class
        
        return render(request,self.template_name,{"form":form_instance, "data":qs})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            Expense.objects.create(**data,owner=request.user)
            
            return redirect("index")
        
        return render(request,self.template_name,{"form":form_instance})
        
        
@method_decorator(decs,name="dispatch")
        
class ExpenseDeleteView(View):
    
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        
        Expense.objects.get(id=id).delete()
        
        return redirect("index")
        
@method_decorator(decs,name="dispatch")

class ExpenseUpdateView(View):
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        Expense.objects.filter(id=id).update()
        
        return redirect("index")

