from django.shortcuts import render
from App.models import Category
from App.models import Sub_Category
def main (request):
    category = Category.objects.all()

    context ={
        'category':category,
    }
    return render(request, 'main.html',context)

def index(request):
    
    return render(request, 'index.html')