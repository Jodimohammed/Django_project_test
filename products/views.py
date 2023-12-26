from django.http  import HttpResponse
from django.shortcuts import render

#/products --> index
def index(request):
    return HttpResponse('hello world')


def new(request):
    return HttpResponse('New Products')