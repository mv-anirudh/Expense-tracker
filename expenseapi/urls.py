from django.urls import path

from expenseapi import views 

urlpatterns=[
    path('signup/',views.UserCreateView.as_view()),
    path('expense/',views.ExpenseListView.as_view()),
    path('expense/<int:pk>',views.ExpenseRetriveUpdateDelte.as_view()),
]