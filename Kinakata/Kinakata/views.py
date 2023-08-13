from itertools import product
from django.shortcuts import redirect, render
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
    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            login(request, new_user)
            return redirect('index')
    else:
        form = UserCreateForm()

        context = {
            'form': form,
        }

    return render(request, 'registration/signup.html', context)
