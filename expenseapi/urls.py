from django.urls import path

from expenseapi import views 

urlpatterns=[
    path('signup/',views.UserCreateView.as_view())
]