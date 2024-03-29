from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Database
from .forms import DatabaseForm, InecForm

# Create your views here.

def home(request):

  return render(request, 'index.html')


def reg(request):
  if request.method == "POST":
    form = DatabaseForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
    #   messages.success(request, Detail.name, "Registered successfully!")
  else:
      form = DatabaseForm()
  return render(request, 'reg.html', {'form': form})

def reg(request):
  if request.method == "POST":
    form = InecForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Details saved successfully!")
    return redirect('home')
  else:
      form = InecForm()
  return render(request, 'reg.html', {'form': form})