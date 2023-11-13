from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def clothes(request):
    return render(request, 'clothes.html')
def men(request):
    return render(request, 'men.html')
def women(request):
    return render(request, 'women.html')
def services(request):
    return render(request, 'services.html')