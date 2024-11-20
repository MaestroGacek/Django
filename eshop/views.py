from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request, template_name= "eshop/intex.html")

def nabidka(request):
    return render(request, template_name= "eshop/nabidka.html")