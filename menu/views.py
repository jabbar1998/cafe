from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Category
from order.forms import CartAddForm
from .forms import SearchForm



# Create your views here.

class Firstview(View):
    def get(self, request, category_slug=None):
        return render(request, 'menu/home.html')


class HomeView(View):
    def get(self, request, category_slug=None):
        form = SearchForm()
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        if 'search' in request.GET:
            form = SearchForm(request.GET)
            if form.is_valid():
                cd = form.cleaned_data['search']
                products = products.filter(name__icontains=cd)

        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'menu/menu.html', {'products': products, 'categories': categories, 'form': form})


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        form = CartAddForm()
        return render(request, 'menu/detail.html', {'product': product, 'form': form})
