from rest_framework import serializers

from expense.models import User,Expense


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model=User
        
        fields=['id','username','email','phone','password']
        
    
    def create(self, validated_data):
        
        return User.objects.create_user(**validated_data)
    
class ExpenseSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model=Expense
        
        fields="__all__"
        
        read_only_fields=['id','create_date','owner']