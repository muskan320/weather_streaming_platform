#import the function that sends weather data to kafka
#and waits for confirmation that the message was delivered
from kafka_producer import publish_and_confirmation


#import the function that fetches weather data
#from the weather API and returns it as an event
from weather_service import get_weather_event