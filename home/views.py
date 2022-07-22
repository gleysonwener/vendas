from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout



def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')


class MyView():
    def get(self, request, *args, **kwargs):
        return render('home3.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')