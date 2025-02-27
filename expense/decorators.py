from django.shortcuts import redirect



def sigin_required(fn):
    
    def wrapper(request,*args,**kwargs):
        
        if not request.user.is_authenticated:
            
            return redirect("signin")
        
        return fn(request,*args,**kwargs)
    
    return wrapper