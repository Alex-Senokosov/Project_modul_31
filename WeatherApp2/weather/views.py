from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# Create your views here.

def index(request):
    appid = '53fa5c6d2e86a32041518a40630562d7'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    if (request.method == "POST"):
        form = CityForm(request.POST)
        form.save()
    form = CityForm



    cities = City.objects.all()
    all_cities =[]
    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {'city': city.name,
                     'temp': res["main"]["temp"],
                     'icon': res["weather"][0]["icon"]
                     }
        all_cities.append(city_info)
    context =  {"all_info":all_cities, "form":form}


    return render(request,'weather/index.html', context)