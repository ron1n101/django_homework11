from django.shortcuts import render
from django.http import HttpResponse

def tag (request):
    html = '<html><body><h1>Hello! You are in app "Tag"</h1></body></html>'
    return HttpResponse(html)