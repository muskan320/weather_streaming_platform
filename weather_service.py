#base URL of the Open - Meteo Weather API
#This API provides the live weather information
BASE_URL= "https://api.open-meteo.com/v1/forecast"

#stores the city details in dictionary
#we use latitude and logitude because API requires coordinates
CITY= {
    "name":"shimla",
    "latitude":31.10,
    "longitude":77.17
}


#Fuction to build a complete API URL
def build_weather_url():
    "open meteo api url"

    #Get the latitude and longitude of the selected city
    latitude=CITY["latitude"]
    longitude=CITY["longitude"]

    #create API request URL using f-string
    #request current temperature,humidity,windspeed, and pressure
    url=(
    f"{BASE_URL}"
    f"?latitude={latitude}"
    f"&longitude={longitude}"
    f"&current=temperature_2m,relative_humidity_2m,"
    f"wind_speed_10m,pressure_msl"
)
    #Return the complete URL
    return url


#Import requests librabry to make HTTP reuqests
import requests

#function to fetch weather data from the API
def fetch_weather_data():

    #generate the API URL
    url=build_weather_url()

    #Send a GET reuqest to weather API

    response = requests.get(url, timeout=10)

    print("API Status:", response.status_code)

    #raise an error if request fails
    response.raise_for_status()

    #convert the API response from json to PYTHON dictionary
    return response.json()
    ## json.dumps(value): we are converting our python ob into json

## create weather event function
from datetime import datetime
def create_weather_event(weather_data):
    current=weather_data["current"]
    event={
    "city":CITY["name"],
    "temperature_c":current["temperature_2m"],
    "humidity_percent":current["relative_humidity_2m"],
    "wind_speed_kmh":current["wind_speed_10m"],
    "pressure_hpa":current["pressure_msl"],
    "event_time":current["time"],
    "producer_timestamp":datetime.now().isoformat()
}
    return event

#function to get the final weather event
def get_weather_event():

    #fetch the raw weather data from API
    weather_data=fetch_weather_data()

    #converts the raw dar into formatted weather evet
    weather_event=create_weather_event(weather_data)
    return weather_event

