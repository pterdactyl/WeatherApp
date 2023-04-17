from django.db import models

# Create your models here.

class UserData(models.Model):
    IP_address = models.CharField(max_length=20)
    IP_type = models.CharField(max_length=10)
    conti_code = models.CharField(max_length=5)
    conti_name = models.CharField(max_length=20)
    count_code = models.CharField(max_length=5)
    count_name = models.CharField(max_length=40)
    region_name = models.CharField(max_length=30)
    region_code = models.CharField(max_length=5)
    city = models.CharField(max_length=30)
    zip = models.CharField(max_length=10)

class WeatherData(models.Model):
    location = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    country = models.CharField(max_length=40)
    timezone = models.CharField(max_length=30)
    local_time = models.DateTimeField(auto_now=True)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)

class AirData(models.Model):
    CO = models.CharField(max_length=20)
    NO = models.CharField(max_length=20)
    Ozone = models.CharField(max_length=20)
    SO = models.CharField(max_length=20)
    fine_particulates = models.CharField(max_length=20)
    ultra_fine = models.CharField(max_length=20)
    EPA_index = models.CharField(max_length=20)
    AirQuality_index = models.CharField(max_length=20)

class WindData(models.Model):
    c_temp = models.DecimalField(decimal_places=1, max_digits=5)
    f_temp = models.DecimalField(decimal_places=1, max_digits=5)
    humidity = models.CharField(max_length=20)
    c_feel = models.DecimalField(decimal_places=1, max_digits=5)
    f_feel = models.DecimalField(decimal_places=1, max_digits=5)
    windspeed_kph = models.DecimalField(decimal_places=1, max_digits=5)
    windspeed_mph = models.DecimalField(decimal_places=1, max_digits=5)
    wind_direction = models.CharField(max_length=10)
    wind_degree = models.IntegerField()
    precipitation_mm = models.CharField(max_length=20)
    precipitation_in = models.CharField(max_length=20)

class GeneralData(models.Model):
    last_updated = models.DateTimeField(auto_now=True)
    timeofDay = models.CharField(max_length=10)
    cloud = models.IntegerField()
    condition = models.ImageField()
    UV = models.CharField(max_length=10)
    visibility_km = models.DecimalField(decimal_places=1, max_digits=5)
    visibility_miles = models.DecimalField(decimal_places=1, max_digits=5)
    pressure_mb = models.DecimalField(decimal_places=1, max_digits=10)
    pressure_water = models.DecimalField(decimal_places=2, max_digits=10)
