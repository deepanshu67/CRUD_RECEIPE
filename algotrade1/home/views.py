from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home/index.html")


def sucess_page(request):
    return render(request)
