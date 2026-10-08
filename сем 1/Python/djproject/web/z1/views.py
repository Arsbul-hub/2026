from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from z1.dao import temp_data
from z1.forms import LoginForm, RegisterForm
def index(request):
    return render(request, "index.html")


def shop(request):
    product_name = request.GET.get("product_name")
    product = None
    if product_name:
        for pname in temp_data["shop"]["products"]:
            if product_name in pname:
                product = pname
                break
    return TemplateResponse(request, "shop.html",
                            {"product_name": product_name,
                             "product": product,
                             "products_list": temp_data["shop"]["products"]
                             })

def register(request):
    register_form = RegisterForm()
    return TemplateResponse(request, "register.html", {"form": register_form})

def login(request):
    login_form = LoginForm()
    return TemplateResponse(request, "login.html", {"form": login_form})

def contacts(request):
    return render(request, "contacts.html")
