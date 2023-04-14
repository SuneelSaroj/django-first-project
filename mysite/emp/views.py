from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def emp_home(request):
    return render(request, "emp/home.html", {})


def add_emp(request):
    if request.method == "POST":
        print("data is coming")
        return redirect("/employee/home/")
    return render(request, "emp/add_emp.html", {})

#this is 
