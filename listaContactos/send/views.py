from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):

    send_mail('Hello from Emanuel',
    'Hello there. This is an automated message.',
    'ehilacondob@unsa.edu.pe',
    ['cikitih105@iridales.com'],
    fail_silently=False)

    return render(request, 'send/index.html')