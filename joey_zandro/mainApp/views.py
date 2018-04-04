from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# Главная страница
def main_page(request):
    return render(request, 'mainApp/templates/main_page.html')


# страница 'About'
def about_page(request):
    return render(request, 'mainApp/templates/about.html')


# страница со списком товаров
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'mainApp/templates/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })


# страница товара
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'mainApp/templates/product_detail.html', {'product': product})


