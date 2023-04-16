from django.shortcuts import render
from .models import Meals, Category, Reservation
from .forms import ReserveTableForm

# Create your views here.

def home(request):

    return render(request, 'home.html')

def about(request):

    return render(request, 'about.html')

def meal_list(request):
    meal_list = Meals.objects.all()
    categories = Category.objects.all()

    context = {
        'meal_list' : meal_list ,
        'categories' : categories ,
        }

    return render(request, 'list.html', context)


def meal_detail(request, slug):
    meal_detail = Meals.objects.get(slug=slug)

    context = {'meal_detail' : meal_detail ,}

    return render(request, 'detail.html', context)


def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()
    
    context = {'form' : reserve_form}

    return render(request, 'reservation.html', context)