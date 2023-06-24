from django.shortcuts import render

# Create your views here.
def add_cart(request):
    return render(request, 'store/add_html')

def cart(request):
    return render(request, 'store/cart.html')

 