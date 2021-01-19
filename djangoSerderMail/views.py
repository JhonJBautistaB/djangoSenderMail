from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives, send_mail

def index(request):
    return render(request, 'index.html', {})


def form_email(request):

    if request.method == 'POST':
        from_email = request.POST.get('from')
        from_to = request.POST.get('to')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print(f'de: {from_email}, para: {from_to}, asunto: {subject}, mensaje: {message}')

        if from_email and from_to and subject:
            email = send_email(from_email, from_to, subject, message)           
        else:
            alert = 'verify the email information'
            return render(request, 'form_email.html', {})

    return render(request, 'form_email.html', {})


def send_email(from_email, from_to, subject, message):
    email = EmailMultiAlternatives(
                subject,                
                message,
                from_email,
                [from_to]
            )
    email.send()
    return f'Su mensaje fue enviado'


def conf_email(request):
    pass