import time
import logging

# Import functions from kafka_producer
from .kafka_producer import (
    publish_and_confirmation,
    close
)

# Import function from weather_service
from .weather_service import (
    get_weather_event
)


def run_weather_producer():
    while True:
        print("Fetching weather...")

        event = get_weather_event()
        print("Event:", event)

        metadata = publish_and_confirmation(
            event,
            key=event["city"]
        )

        print("Sent Successfully!")
        print(metadata)

        time.sleep(30)


if __name__ == "__main__":
    try:
        run_weather_producer()

    except KeyboardInterrupt:
        logging.info("Producer stopped by user.")

    finally:
        close()