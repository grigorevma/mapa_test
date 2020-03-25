from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import  SignUpForm
from django.http import HttpResponse

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/ok")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class OkView(View, LoginRequiredMixin):
    def get(self, request):
        return HttpResponse("OK")

class HomeView(View, LoginRequiredMixin):
    def get(self, request):
        return redirect("/signup")