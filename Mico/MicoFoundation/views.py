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
