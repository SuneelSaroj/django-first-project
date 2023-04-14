from django.http import HttpResponse
import datetime

from django.shortcuts import render


def home(request):

    # this is getting data using request
    if request.method == 'POST':
        check = request.POST['check']
        print(check)

    # this is a dynamic data
    college_name = "Django College"
    list_of_books = ["Python", "Django", "Java", "C++", "C"]
    student_name = ["Sunil", "Tanishq"]
    student_marks = [10, 20]

    student = {
        "student_name": student_name,
        "books": list_of_books,
        "marks": student_marks
    }
    data = {
        "college_name": college_name,
        "student_data": student,

    }

    # return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>" + str(now))
    return render(request, "home.html", data)


def about(request):
    # return HttpResponse("<h1>This is About page</h1>")
    return render(request, "about.html", {})


def service(request):
    # return HttpResponse("<h1>This is Services page</h1>")
    return render(request, "service.html", {})
