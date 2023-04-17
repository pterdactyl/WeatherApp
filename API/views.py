from django.shortcuts import render
import requests
from FinalExam import views
from django.db import connection


# Create your views here.

def user(request):
    views.getData(request)
    weather = getWeather()
    air = getAirData()
    temperature = getWind()
    general = getGeneral()
    user = getUser()
    context = {
        'weather': weather,
        'air': air,
        'temperature': temperature,
        'general': general,
        'user': user
    }
    url = 'API/current.html' \
        if request.resolver_match.url_name == 'current' \
        else 'API/remote.html'

    return render(request, url, context)

def getUserData(request):
    if not request.session.get('userinfo_fetched', False):
        url = 'http://api.ipstack.com/check?access_key=581cd44f042e4e660978ce2f63a38095'
        response = requests.get(url)
        request.session['userinfo'] = response.json()
        request.session['userinfo_fetched'] = True
    return request.session['userinfo']


def getWeatherData(request):
    baseurl = 'http://api.weatherapi.com/v1/current.json?key=aee56a3f10764beeb83232159231404&q='

    if request.method == 'GET':
        current = request.GET.get('location')
    else:
        current = getUserData(request)["city"]

    if current == '' or current == None:
        current = getUserData(request)["city"]

    aqi = '&aqi=yes'

    url = baseurl + current + aqi
    print(url)
    response = requests.get(url)
    data = response.json()
    return data


def getWeather():
    cur = connection.cursor()
    command = "SELECT location, region, country, timezone, local_time, latitude, longitude FROM API_weatherdata WHERE id = (SELECT  MAX(id) FROM API_weatherdata) "
    cur.execute(command)
    return dictfetchall(cur)


def getUser():
    cur = connection.cursor()
    command = "SELECT IP_address, IP_type, conti_code,  conti_name, count_code, count_name, region_name, region_code, city, zip FROM API_userdata WHERE id = (SELECT  MAX(id) FROM API_userdata) "
    cur.execute(command)
    return dictfetchall(cur)


def getAirData():
    cur = connection.cursor()
    command = "SELECT CO, `NO`, Ozone, SO, fine_particulates, ultra_fine, EPA_index, AirQuality_index FROM API_airdata WHERE id = (SELECT  MAX(id) FROM API_airdata) "
    cur.execute(command)
    return dictfetchall(cur)


def getWind():
    cur = connection.cursor()
    command = "SELECT c_temp, f_temp, humidity,  c_feel, f_feel, windspeed_kph, windspeed_mph, wind_direction, wind_degree, precipitation_mm, precipitation_in FROM API_winddata WHERE id = (SELECT  MAX(id) FROM API_winddata) "
    cur.execute(command)
    return dictfetchall(cur)


def getGeneral():
    cur = connection.cursor()
    command = "SELECT last_updated, timeofDay, cloud,`condition`, UV, visibility_km, visibility_miles, pressure_mb, pressure_water FROM API_generaldata WHERE id = (SELECT  MAX(id) FROM API_generaldata) "
    cur.execute(command)
    return dictfetchall(cur)


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]