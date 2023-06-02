from django.shortcuts import render,redirect
from django.contrib.auth import forms
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerUserCreationForm


# Create your views here.
def register(request):
    if request.POST == 'POST':
        form = CustomerUserCreationForm()
        if form.is_valid():
            form.save()
    else:
        form = CustomerUserCreationForm()
        context = {
            'form':form
        }
    return render(request,'register.html',context)
