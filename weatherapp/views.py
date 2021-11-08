from django.shortcuts import render
import urllib
import json


def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        url = 'http://api.openweathermap.org/data/2.5/weather?q='+ city + '&units=metric&appid=211eb9213e87d848e827b7f0d2517393'
        api_url = urllib.request.urlopen(url)
        api_data = api_url.read()
        json_data = json.loads(api_data)
        print(json_data)

        data = {
            'city': city,
            'description': json_data['weather'][0]['description'],
            'icon': json_data['weather'][0]['icon'],
            'temperature': json_data['main']['temp'],
            'pressure': json_data['main']['pressure'],
            'humidity': json_data['main']['humidity'],
            'timezone':  json_data['sys']['country']
        }
    else:
        data = {
            'city': None,
            'description': None,
            'icon': None,
            'temperature': None,
            'pressure': None,
            'humidity': None
        }
    return render(request, 'index.html', {'data': data})
