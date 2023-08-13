from itertools import product
from django.shortcuts import render
from App.models import Category, Product


def main(request):

    return render(request, 'main.html')


def index(request):
    category = Category.objects.all()

    product = Product.objects.all()

    context = {
        'category': category,

        'product': product,
    }
    return render(request, 'index.html', context)
