from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product

def all_products(request):
    products = Product.objects.all()  # fetch all products
    return render(request, 'products/all_products.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_products')  # redirect to the product list page
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
