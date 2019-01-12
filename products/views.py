import random
from django.shortcuts import render
from django.db.models import Q
from .models import Product

brands = {
    'jansport': 'JS',
    'sprayground': 'SG',
    'slazenger': 'SL',
    'alentino': 'AL',
    'samsonite': 'SS',
    'high-sierra': 'HS',
    'wilson': 'WI'
}
types = {
    'luggage': 'LG',
    'lunchbags': 'LB'
}

def get_random_bags(n=15):
    bags = list(Product.objects.all())
    random.shuffle(bags)
    random_bags = bags[:n]

    return random_bags

def home(request):
    random_bags = get_random_bags()
    return render(request, 'index.html', {'bags': random_bags})


def findus(request):
    return render(request, 'findus.html', {})

def other_products(request):
    bags = Product.objects.all().exclude(Q(brand='JS') | Q(brand='SG'))
    return render(request,'showcase.html',{'bags':bags})

def accessories(request):
    bags = Product.objects.all().filter(Q(type='LB') |Q(type='PB'))
    return render(request, 'showcase.html', {'bags': bags})

def get_bags(request):
    cate = request.path.replace('/', '')
    if cate in brands.keys():
        bags = Product.objects.all().filter(brand=brands[cate])
    elif cate in types.keys():
        bags = Product.objects.all().filter(type=types[cate])
    else:
        bags = {}

    return render(request, 'showcase.html', {'bags': bags})

def get_product(request, cate, id):
    bag = Product.objects.get(id=id)
    return render(request, 'product.html', {'bag': bag})

def get_product_index(request, id):
    bag = Product.objects.get(id=id)
    return render(request, 'product.html', {'bag': bag})