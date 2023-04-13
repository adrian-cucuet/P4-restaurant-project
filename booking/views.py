from django.shortcuts import render
from .models import Meals

# Create your views here.

def meal_list(request):
    meal_list = booking.objects.all()

    context = {'meal_list' : meal_list ,}

    return render(request , 'booking/list.html' , context)


def meal_detail(request, slug):
    pass