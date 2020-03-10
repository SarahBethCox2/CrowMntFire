from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/home.html')

def aboutus(request):
    return render(request, 'pages/aboutus.html')

def contactus(request):
    return render(request, 'pages/contactus.html')

def volunteer(request):
    return render(request, 'pages/volunteer/volunteer.html')

def burnnotice(request):
    return render(request, 'pages/burnnotice/burnnotice.html')

def events(request):
    return render(request, 'pages/events.html')

def educational(request):
    return render(request,'pages/educational.html')