from django.shortcuts import render
from cms.models import CmsSlider
from .models import Order


# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()
    return render(request, "./index.html", {"slider_list": slider_list})


def thanks_page(request):
    name = request.POST["name"]
    phone = request.POST["phone"]
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(
        request,
        "./thanks_page.html",
        {
            "name": name,
            "phone": phone,
        },
    )
