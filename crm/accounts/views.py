from django.shortcuts import render, redirect

from .forms import OrderForm, CustomerForm, ProductForm
from .models import Order, Customer, Product


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders':orders,'customers':customers,'total_orders':total_orders,'delivered':delivered,'pending':pending,
        'total_customers': total_customers
    }

    return render(request, 'accounts/dashboard.html' , context)

def Customers(request,pk):

    customer = Customer.objects.get(pk=pk)

    orders = customer.order_set.all()
    order_count=orders.count()

    context = {'customer':customer ,'orders':orders, 'order_count':order_count}

    return render(request, 'accounts/customers.html', context)


def Products(request):

    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products':products})


def createOrder(request):
    form =OrderForm()
    if request.method == 'POST' :
        form =OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)



def createCustomer(request):
    forma =CustomerForm()
    if request.method == 'POST' :
        forma =CustomerForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect('/')

    context = {'forma': forma}
    return render(request, 'accounts/customer_form.html', context)


def createProduct(request):
    form_product = ProductForm()
    if request.method == 'POST' :
        form_product = ProductForm(request.POST)
        if form_product.is_valid():
            form_product.save()
            return redirect('/')

    context = {'form_product': form_product,}
    return render(request, 'accounts/product_form.html', context)
