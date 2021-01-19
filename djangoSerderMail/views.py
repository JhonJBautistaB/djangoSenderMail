from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'index.html', {})


def form_email(request):
    return render(request, 'form_email.html', {})


def send_email(request):
    if request.method == 'POST':
        by_email = request.POST.get('to')
        cc_email = request.POST.get('cc')
        subject = request.POST.get('subject')


        print('Se envió correo')

    return render(request, 'index.html', {})