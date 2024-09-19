from django.shortcuts import render
from . models import Cetegory, Product
# Create your views here.


def store (request):
    all_products = Product.objects.all()

    context = {'all_products': all_products}


    return render(request, 'store/store.html', context)

def categories(request):

    all_categories = Cetegory.objects.all()

    return{'all_categories': all_categories}