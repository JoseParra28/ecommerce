from django.shortcuts import render
from . models import Cetegory
# Create your views here.


def store (request):
    return render(request, 'store/store.html')

def categories(request):

    all_categories = Cetegory.objects.all()

    return{'all_categories': all_categories}