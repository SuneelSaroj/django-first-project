from django.contrib import admin
from django.urls import path, include
from emp.views import *


urlpatterns = [
    path("home/", emp_home),
    path("add-emp/",add_emp)

]
