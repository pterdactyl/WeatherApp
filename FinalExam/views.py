#  Copyright (c) 2023 - All rights reserved.
#  Created by Peter Lin for PROCTECH 4IT3/SEP 6IT3.
#
#  SoA Notice: I Peter Lin, 400270145 certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

from django.shortcuts import render
import os
import mysql.connector
from FinalExam.settings import BASE_DIR
from API import views
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
    if request.user.is_authenticated:
        print("Welcome")
    else:
        print("Denied")

    return redirect('current/')


def getData(request):
    cnx = mysql.connector.connect(read_default_file=str(os.path.join(BASE_DIR, 'configs', 'my.cnf')))
    cur = cnx.cursor()
    data = views.getWeatherData(request)
    data1 = views.getUserData(request)

    co = data["current"]["air_quality"]['co']
    no = data["current"]["air_quality"]['no2']
    ozone = data["current"]["air_quality"]['o3']
    so = data["current"]["air_quality"]['so2']
    fine = data["current"]["air_quality"]['pm2_5']
    ultra = data["current"]["air_quality"]['pm10']
    EPA = data["current"]["air_quality"]['us-epa-index']
    eu = data["current"]["air_quality"]['gb-defra-index']
    cur.execute('insert into API_airdata (CO, `NO`, Ozone, SO, fine_particulates, ultra_fine, EPA_index, AirQuality_index) values'
                    ' (%s,%s,%s,%s,%s,%s,%s,%s)', (co, no, ozone, so, fine, ultra, EPA, eu))

    update = data["current"]["last_updated"]
    isday = data["current"]["is_day"]
    cloud = data["current"]["cloud"]
    condition = data["current"]["condition"]["icon"]
    uv = data["current"]["uv"]
    vis_km = data["current"]["vis_km"]
    vis_miles = data["current"]["vis_miles"]
    pressure_mb = data["current"]["pressure_mb"]
    pressure_in = data["current"]["pressure_in"]
    if isday == 0:
        isday = 'Night Time'

    else:
        isday = 'Day Time'

    cur.execute('insert into API_generaldata (last_updated, timeofDay, cloud,`condition`, UV, visibility_km, visibility_miles, pressure_mb, pressure_water) values'
        ' (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (update, isday, cloud, condition, uv, vis_km, vis_miles, pressure_mb, pressure_in))

    location = data["location"]["name"]
    region = data["location"]["region"]
    country = data["location"]["country"]
    timezone = data["location"]["tz_id"]
    localtime = data["location"]["localtime"]
    lat = data["location"]["lat"]
    lon = data["location"]["lon"]

    cur.execute(
        'insert into API_weatherdata (location, region, country, timezone, local_time, latitude, longitude) values'
        ' (%s,%s,%s,%s,%s,%s,%s)',(location, region, country, timezone, localtime, lat, lon))

    temp_c = data["current"]["temp_c"]
    temp_f = data["current"]["temp_f"]
    humidity = data["current"]["humidity"]
    feelslike_c = data["current"]["feelslike_c"]
    feelslike_f = data["current"]["feelslike_f"]
    wind_kph = data["current"]["wind_kph"]
    wind_mph = data["current"]["wind_mph"]
    wind_dir = data["current"]["wind_dir"]
    wind_degree = data["current"]["wind_degree"]
    precip_mm = data["current"]["precip_mm"]
    precip_in = data["current"]["precip_in"]

    cur.execute(
        'insert into API_winddata (c_temp, f_temp, humidity,  c_feel, f_feel, windspeed_kph, windspeed_mph, wind_direction, wind_degree, precipitation_mm, precipitation_in) values'
        ' (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (temp_c, temp_f, humidity, feelslike_c, feelslike_f, wind_kph, wind_mph, wind_dir, wind_degree, precip_mm, precip_in))


    ip = data1["ip"]
    type = data1["type"]
    continent_code = data1["continent_code"]
    continent_name = data1["continent_name"]
    country_code = data1["country_code"]
    country_name = data1["country_name"]
    region_name = data1["region_name"]
    region_code = data1["region_code"]
    city = data1["city"]
    zip = data1["zip"]


    cur.execute(
        'insert into API_userdata (IP_address, IP_type, conti_code,  conti_name, count_code, count_name, region_name, region_code, city, zip) values'
        ' (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (ip, type, continent_code, continent_name,country_code, country_name, region_name, region_code, city, zip))

    cnx.commit()
    cnx.close()