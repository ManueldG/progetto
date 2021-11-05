from django.shortcuts import render

from django.http import HttpResponse


def view_a(request):
    return HttpResponse("""
    <h1>home<h1>

    <ul>
        <li>
        <a href="/">home<a>
        </li>

        <li>
        <a href="nome_app/view_b">vista b<a>
        </li>

        <li>
        <a href="nome_app/view_c">vista c<a>
        </li>
    </ul
    
    """)

def view_b(request):
    return HttpResponse("""
    <h1>view b<h1>

    <ul>
        <li>
        <a href="/">home<a>
        </li>

        <li>
        <a href="view_b">vista b<a>
        </li>

        <li>
        <a href="view_c">vista c<a>
        </li>
    </ul
    
    """)

def view_c(request):
    return HttpResponse("""
    <h1>view c<h1>
    <ul>
        <li>
        <a href="/">home<a>
        </li>

        <li>
        <a href="../view_b">vista b<a>
        </li>

        <li>
        <a href="../view_c">vista c<a>
        </li>
    </ul>
    
    """)