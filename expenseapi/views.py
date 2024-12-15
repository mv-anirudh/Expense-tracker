from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from expenseapi.serializer import UserSerializer



class UserCreateView(APIView):
    serializer_calss=UserSerializer
    
    def post(self,request,*args,**kwargs):
        
        serializer_instance=self.serializer_calss(data=request.data)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
    
