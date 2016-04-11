from django.shortcuts import render

# Create your views here.

from  django.http import  StreamingHttpResponse
from  rest_framework.renderers import  JSONRenderer
from  dtr.models import Book
from  dtr.book_serializers import BookSerializer

from rest_framework.views import  APIView
from rest_framework.response import  Response
from rest_framework import  generics
from dtr.pyredis import pyRedis

# class JSONResponse(StreamingHttpResponse):
#     def __init__(self,data,**kwargs):
#         centent = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse,self).__init__(data,**kwargs)
#
#
# def book_list(request,num):
#     if request == 'GET':
#         b = Book.objects.get(id=num)
#         ser = BookSerializers(b)
#
#         print  JSONResponse(ser.data)
#         return  JSONResponse(ser.data)
#         # print JSONResponse(ser.data)



class Booklist(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(APIView):
    def get(self,request,num,formt=None):
        b = Book.objects.get(id=num)
        print  b.author
        ser = BookSerializer(b.author)
        print  ser
        print  ser.data
        return Response(ser.data)

class get_redis(APIView):
    def get(self,request,parameter,format=None):
        redis_value = pyRedis().get_key(parameter)
        return  Response(redis_value)


