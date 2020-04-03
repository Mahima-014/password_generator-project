from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    return render(request,'generator/home.html')
def about(request):
    return render(request,'generator/about.html')

def password(request):
    c = list('abcdefghijklmnopqrst')
    if request.GET.get('uppercase'):
        c.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        c.extend(list('1234567890'))
    if request.GET.get('special'):
        c.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length',12))
    the_pass=''
    for i in range(length):
        the_pass+=random.choice(c)

    return render(request,'generator/password.html',{'password':the_pass})

# Create your views here.
