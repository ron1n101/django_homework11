from django.shortcuts import render
from django.http import HttpResponse

def post (request):
    html = '<html><body><h1>Hello! You are in app "Post"</h1></body></html>'
    return HttpResponse(html)


