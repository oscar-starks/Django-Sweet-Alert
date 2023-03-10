from django.shortcuts import render
from django.contrib import messages

def indexView(request):
    html_page  = "index.html"
    messages.success(request, "This is the success message")
    return render(request, html_page)
