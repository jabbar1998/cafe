from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import View
from .cart import Cart
from menu.models import Product
from .forms import CartAddForm
from .models import Order, OrderItem, Table


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'order/cart.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
        return redirect('order:cart')


class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('order:cart')


class OrderCreateView(View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create()
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        cart.clear()
        return redirect('order:order_detail', order.id)



class OrderDetailView(View):

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        cart = OrderItem.objects.filter(order=order_id)
        tables = Table.objects.filter(availability=True)
        return render(request, 'order/checkout.html', {'order': order, 'cart': cart, 'tables': tables})

    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        customer_number = request.POST.get('customer_number')
        order_description = request.POST.get('additional_info')
        customer_table_id = request.POST.get('selected_table')
        
        if customer_number and order_description and customer_table_id:
            order.customer_phone_number = customer_number
            order.description = order_description
            try:
                table = Table.objects.get(id=customer_table_id, availability=True)
                order.table = table
                order.save()
                table.availability = False
                table.save()
            except Table.DoesNotExist:
                
                order.save()
            # reverse('order:order_confirmation', args=[order_id]
            return HttpResponse('order complete')
            
        # return render(request, 'order/checkout.html', {'order': order})
    
