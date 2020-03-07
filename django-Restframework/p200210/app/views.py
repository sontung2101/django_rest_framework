from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def hello(request):
    return Response({"message" : "hello"})  

@api_view(['GET'])
def getProducts(request):
    products=[
        {'id':1,'code':'0001','name':'Product 1'},
        {'id':2,'code':'0002','name':'Product 2'},
        {'id':3,'code':'0003','name':'Product 3'},
        {'id':4,'code':'0004','name':'Product 4'},
    ]
    return Response({'products':products})