from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'London'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=xxxxxx'
    PARAMS = {'units':'metric'}

    API_KEY = '55924d3e30b754d27505b4a5313eda67'
    SEARCH_ENGINE_ID = '07e6c528b0ac242a9'

    # query = city +  " 1920x1080"
    # page = 1
    # start = (page - 1) * 10 + 1
    # searchType = 'image'
    # city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    try:
        weather_data = requests.get(url, PARAMS).json()
        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        temp = weather_data['main']['temp']
        day = datetime.date.today()

        # city_data = requests.get(city_url).json()
        # image_url = city_data['items'][0]['link']

        return render(request, 'index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city, 'exception_occurred':False})

    except:
        messages.error(request, 'City not found')
        day = datetime.date.today()
        return render(request, 'index.html', {'day': day, 'exception_occurred':True})
