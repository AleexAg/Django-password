from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'about.html')


def password(request):
    chars = list('abcdefghijklmnopqrstuvwxyz')
    generate = ''

    can = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        chars.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        chars.extend('@*&#()!^$-_+')
    if request.GET.get('num'):
        chars.extend('1234567890')

    for char in range(can):
        generate += random.choice(chars)


    return render(request, 'password.html', {
        'password': generate
    })
