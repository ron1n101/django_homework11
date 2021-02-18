from django.shortcuts import render
from django.http import HttpResponse

def editor (request):
    html = '<html><body><h1>Hello! You are in app "Editor"</h1></body></html>'
    return HttpResponse(html)