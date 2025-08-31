from django.shortcuts import render
from . models import Property,Rent,shortlet,Buy,Land
from django.core.paginator import Paginator
# Create your views here.
def base(request):
    return render(request,'base.html')


def home(request):
    props = Property.objects.all()

    contexts ={
        'props':props
    }
    return render(request,'service/home.html',contexts)

def about(request):
    props = Property.objects.all()

    contexts ={
        'props':props
    }
    return render(request,'service/about.html',contexts)

def rent(request):
    rents = Rent.objects.all()
    paginator = Paginator(rents, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'service/rent.html', {
        'page_obj': page_obj,  
    })


def buy(request):
    buys = Buy.objects.all()
    paginator = Paginator(buys, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'service/buy.html', {
        'page_obj': page_obj,  
    })


def short(request):
    short = shortlet.objects.all()
    paginator = Paginator(short, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'service/shortlet.html', {
        'page_obj': page_obj,  
    })

def land(request):
    land = Land.objects.all()
    paginator = Paginator(land, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'service/land.html', {
        'page_obj': page_obj,  
    })

def contact(request):
    return render(request,'service/contact.html')


