from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world.</h1><p>This is the ethix application.</p>")

def delete(request):
    return HttpResponse("<h1>Delete this page</h1>")