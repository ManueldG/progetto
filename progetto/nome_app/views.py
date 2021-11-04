from django.shortcuts import render

from django.http import HttpResponse


def view_a(request):
    return HttpResponse("<h1>home<h1>")

def view_b(request):
    return HttpResponse("<h1>view b<h1>")

def view_c(request):
    return HttpResponse("<h1>view c<h1>")