# Create your views here.

from django.shortcuts import render

from .models import Order
from .forms import OrderForm


def first_page(request):
    order_list = Order.objects.all()
    form = OrderForm()
    return render(request,
                  './index.html',
                  {
                      'order_list': order_list,
                      'form': form
                  }
                  )


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']

    element = Order(order_name=name, order_phone=phone)
    element.save()

    return render(request, './thanks_page.html')