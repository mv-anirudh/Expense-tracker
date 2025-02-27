"""
URL configuration for expense_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from expense import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.SignUpView.as_view(),name='signup'),
    path('',views.SigninView.as_view(),name='signin'),
    path('signout',views.SignOutView.as_view(),name='signout'),
    path('index',views.IndexView.as_view(),name="index"),
    path('<int:pk>/remove',views.ExpenseDeleteView.as_view(),name="delete"),
    path('update/<int:pk>/change/',views.ExpenseUpdateView.as_view(),name="update"),
    path('api/',include('expenseapi.urls'))
]
    
