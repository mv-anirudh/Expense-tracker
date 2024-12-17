from django.shortcuts import get_object_or_404, render
from expense.models import Expense
from rest_framework.views import APIView
from rest_framework import status,authentication,permissions
from rest_framework.response import Response
from expenseapi.serializer import UserSerializer,ExpenseSerializer
from rest_framework import serializers




class UserCreateView(APIView):
    serializer_calss=UserSerializer
    
    def post(self,request,*args,**kwargs):
        
        serializer_instance=self.serializer_calss(data=request.data)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ExpenseListView(APIView):
    
    authentication_classes=[authentication.BasicAuthentication]
    permissions_calsses=[permissions.IsAdminUser]
    
    serializer_class=ExpenseSerializer
  
    def get (self,request,*args,**kwargs):
        
        qs=Expense.objects.filter(owner=request.user)
        
        if "status" in request.query_params:
            
            search_text=request.query_params.get("status")
            
            qs=qs.filter(status=search_text)
        
        serializer_instance=self.serializer_class(qs,many=True)
        
        return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)

    def post(self,request,*args,**kwargs):
        
        serializer_instance=self.serializer_class(data=request.data)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save(owner=request.user)
            
            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)
    
    
class ExpenseRetriveUpdateDelte(APIView):
    
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    serializer_class=ExpenseSerializer
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get('pk')
        
        qs=get_object_or_404(Expense,id=id)
        
        serializer_class=self.serializer_class(qs)
        
        return Response(data=serializer_class.data,status=status.HTTP_201_CREATED)
    
    def delete(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        todo_obj=get_object_or_404(Expense,id=id)
        
        if request.user!=todo_obj.owner:
            
            raise serializers.ValidationError("access denied")
        
        todo_obj.delete()
        
        return Response(data={"message":"deleted"})
    
    def put(self,request,*args,**kwargs):
        
        id=kwargs.get('pk')
        
        todo_obj=get_object_or_404(Expense,id=id)
        
        if request.user != todo_obj.owner:
            raise serializers.ValidationError("acess denied")
        
        serializer_instance=self.serializer_class(data=request.data,instance=todo_obj)
        
        if serializer_instance.is_valid():

            serializer_instance.save(owner=request.user)
            
            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)
            
        
        