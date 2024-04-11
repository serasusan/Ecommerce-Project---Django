from django.shortcuts import render, HttpResponse,redirect
from .models import Product, Category, Review
from .forms import ProductForm, CategoryForm, ReviewForm


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    review = Review.objects.filter(product=product)
    return render(request, 'product_details.html', {'product': product,'review':review})

def create_product(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        
    context = {'form': form}
    return render(request, 'product_form.html', context)

def update_product(request,pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail',pk=pk)

    context = {'form':form}
    return render(request,'product_form.html',context)

def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)    
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    context = {'object':product}
    return render(request,'delete.html',context)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories':categories})

def createCategory(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        
    context = {'form': form}
    return render(request,'category_form.html',context)

def updateCategory(request,pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance = category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    
    context = {'form':form}
    return render(request,'category_form.html',context)

def deleteCategory(request,pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    
    context = {'object':category}
    return render(request,'delete.html',context)

def home(request):
    return render(request, 'home.html')


def createReview(request,pk):
    review = Review.objects.get(id=pk)
    form = ReviewForm(initial={'product':pk})

    if request.method == 'POST':
        form = ReviewForm()
        if form.is_valid():
            form.save()
            return redirect('product_list')
        
    context = {'form': form,'product':pk}
    return render(request, 'review_form.html', context)

def updateReview(request,pk):
    review = Review.objects.get(id=pk)
    form = ReviewForm(initial={'product':pk})

    if request.method == 'POST':

        form = CategoryForm(request.POST, instance = review)
        if form.is_valid():
            form.save()
            return redirect('product/<int:pk>/')
    context = {'form':form,'product':pk}
    # initial
    return render(request,'review_form.html',context)

def deleteReview(request,pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    
    context = {'object':category}
    return render(request,'delete.html',context)

