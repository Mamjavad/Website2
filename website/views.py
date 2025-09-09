from django.shortcuts import render
from django.http import HttpResponse

def index_views(requst):
    return render(requst,'website/index.html')

def About_views(requst):
    return render(requst,'website/About.html')

def contact_views(requst):
    return render(requst,'website/contact.html')