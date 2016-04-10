from django.shortcuts import render

# Create your views here.

from  django.http import  HttpResponse
from  rest_framework.renderers import  JSONRenderer
from  dtr.models import Book
from  dtr.serializers import  BookSerializers

class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        centent = JSONResponse().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse,self).__init__(data,**kwargs)


def book_list(request):
    b = Book.objects.all()
    ser = BookSerializers(b)
    return  JSONRenderer(ser.data)