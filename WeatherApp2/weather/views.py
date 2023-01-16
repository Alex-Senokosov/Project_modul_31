from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    appid = '0fedf62a4b48093d0fe6e0b95fe05ae2'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = "Minsk"
    res = requests.get(url.format(city))
    print(res.text)




    return render(request,'weather/index.html')