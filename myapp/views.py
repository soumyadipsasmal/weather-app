from django.shortcuts import render
import requests


# Create your views here.
def home(request):
    city = request.GET.get('city', "Kolkata")
     
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5d64f1cf2105319fa8cb35dae5f04e27' 
    response = requests.get(url) 
    data = response.json()  
    payload = {
    'city': data['name'],
    'weather': data['weather'][0]['main'],
    'icon': data['weather'][0]['icon'],
    'kelvin_temperature': data['main']['temp'],
    'celcius_temperature': int(data['main']['temp'] - 273), 
    'pressure': data['main']['pressure'],
    'humidity': data['main']['humidity'],
    'description': data['weather'][0]['description'],
}

    context = {'data': payload}
    
   
    return render(request, 'home.html',context)