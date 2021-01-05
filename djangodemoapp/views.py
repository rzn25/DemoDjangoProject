from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def add_form(request, **kwargs):
    return render(request,"add_numbers.html")

def show_result(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_number=request.POST.get("number1")
        second_number=request.POST.get("number2")
        try:
            sum = round((float(first_number) + float(second_number)),2)
            messages.success(request,"Successfully Added Numbers")
            return render(request, "add_numbers.html", {'number1': first_number, 'number2' : second_number, 'sum' : sum})
        except:
            messages.error(request,"Failed to Add Numbers")
            return render(request, "add_numbers.html", {'number1': first_number, 'number2' : second_number})