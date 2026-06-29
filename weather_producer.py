import json
import time
import logging

#import the function that sends weather data to kafka
#and waits for confirmation that the message was delivered
from kafka_producer import publish_and_confirmation


#import the function that fetches weather data
#from the weather API and returns it as an event
from weather_service import(
    get_weather_event,
    publish_and_confirmation,
    close
)

def run_weather_producer():
    while True:
        try:
            event=get_weather_event()
            metadata=publish_and_confirmation(
                event,
                key=event["city"]
            )
            logging.info(
                f"""
published sucessfully
Topic: {metadata.topic}
Partition: {metadata.partition}
Offset: {metadata.offset}
"""
     )
        except Exception as e:
            logging.exception(
                f"producer Error:{e}"
            )
        finally:
            time.sleep(30)


        