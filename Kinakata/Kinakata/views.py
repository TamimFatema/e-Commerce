from itertools import product
from django.shortcuts import render
from App.models import Category, Product

from django.contrib.auth import authenticate, login
from App.models import UserCreateForm


def main(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }

    return render(request, 'main.html', context)


def index(request):

    product = Product.objects.all()

    context = {

        'product': product,
    }
    return render(request, 'index.html')


def signup(request):
    return render(request, 'registration/signup.html')
