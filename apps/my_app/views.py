from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def index(request):
    return render(request, 'my_app/index.html')


def submit_survey(request):
    if request.method == "POST":
        if 'count' not in request.session.keys():
            request.session['count'] = 0
        request.session['count'] += 1

        request.session['name'] = request.POST['name']
        request.session['dojoLocation'] = request.POST['dojoLocation']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']



    return redirect('/result')


def result(request):
    return render(request, 'my_app/submitted.html')
