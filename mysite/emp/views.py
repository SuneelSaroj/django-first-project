from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp

# Create your views here.


def emp_home(request):
    emps = Emp.objects.all()

    return render(request, "emp/home.html", {
        "emps": emps
    })


def add_emp(request):
    if request.method == "POST":
        # data fetch
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        is_working = request.POST.get("is_working")
        department = request.POST.get("department")

        # create model object and set data
        e = Emp()
        e.name = name
        e.emp_id = email
        e.mobile = phone
        e.address = address
        e.department = department
        if is_working is None:
            e.is_working = False
        else:
            e.is_working = True

        # save to database
        e.save()

        # prepare massage

        return redirect("/employee/home/")
    return render(request, "emp/add_emp.html", {})


def delete_emp(request, emp_id):
    emp = Emp.objects.get(pk=emp_id)
    emp.delete()

    return redirect("/employee/home/")


def update_emp(request, emp_id):
    emp = Emp.objects.get(pk=emp_id)

    return render(request, "emp/update_emp.html", {
        "emp": emp
    })


def do_update_emp(request, emp_id):

    if request.method == "POST":
        # data fetch
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        is_working = request.POST.get("is_working")
        department = request.POST.get("department")

        e = Emp.objects.get(pk=emp_id)

        # create model object and set data
        e.name = name
        e.emp_id = email
        e.mobile = phone
        e.address = address
        e.department = department
        if is_working is None:
            e.is_working = False
        else:
            e.is_working = True

        # save to database
        e.save()

    return redirect("/employee/home/")
