from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'shoes/index.html')
def about(request):
    return render(request, 'shoes/about.html')
def contact(request):
    return render(request, 'shoes/contact.html')
def shop(request):
    return render(request, 'shoes/shop.html')
def checkout(request):
    return render(request, 'shoes/checkout.html')
def payment(request):
    return render(request, 'shoes/payment.html')
def error(request):
    return render(request, 'shoes/404.html')
def single(request):
    return render(request, 'shoes/single.html')
