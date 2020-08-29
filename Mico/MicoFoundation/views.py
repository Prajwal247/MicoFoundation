from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'MicoFoundation/home.html', {})


def aboutpage(request):
    return render(request, 'MicoFoundation/about.html', {})

def boardmembers(request):
    return render(request, 'MicoFoundation/boardmembers.html', {})

def sponsorship(request):
    return render(request, 'MicoFoundation/sponsorship.html', {})

def contact(request):
    return render(request, 'MicoFoundation/contact.html', {})

def donate(request):
    return render(request, 'MicoFoundation/donate.html', {})

def getinvolved(request):
    return render(request, 'MicoFoundation/getinvolved.html', {})


def history(request):
    return render(request, 'MicoFoundation/history.html', {})


def ladymessage(request):
    return render(request, 'MicoFoundation/ladymessage.html', {})

def managermessage(request):
    return render(request, 'MicoFoundation/managermessage.html', {})

def messagechairman(request):
    return render(request, 'MicoFoundation/messagechairman.html', {})

def newsroom(request):
    return render(request, 'MicoFoundation/newsroom.html', {})
