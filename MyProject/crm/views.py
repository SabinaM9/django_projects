# Create your views here.

from django.shortcuts import render

from .models import Order


def first_page(request):
    order_list = Order.objects.all()
    return render(request,
                  './index.html',
                  {'order_list': order_list}
                  )


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']

    element = Order(order_name=name, order_phone=phone)
    element.save()

    return render(request, './thanks_page.html')