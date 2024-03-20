from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.
def product_list(request):
    return render(request, 'test.html')
#     products = Product.objects.all()
#     return render(request, 'product_list.html', {'products': products})

# def product_detail(request, pk):
#     product = Product.objects.get(pk=pk)
#     return render(request, 'product_details.html', {'product': product})
