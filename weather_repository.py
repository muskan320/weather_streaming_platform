"""
Weather Repository

Responsibility:
Store weather events into MySQL database.

"""

import logging

from database.mysql_connection import (
    connection,
    cursor
)


def insert_weather_event(event):
    """
    Inserts one weather event into the weather_readings table.

    Parameters:
    
    event : dict

    Example:

    {
        "city": "Shimla",
        "temperature_c": 18.5,
        "humidity_percent": 82,
        "wind_speed_kmh": 7.2,
        "pressure_hpa": 1008.4,
        "event_time": "2026-07-18T15:20",
        "producer_timestamp": "2026-07-18T15:20:30"
    }
    """

    try:

        query = """
        INSERT INTO weather_readings (

            city,
            temperature_c,
            humidity_percent,
            wind_speed_kmh,
            pressure_hpa,
            event_time,
            producer_timestamp

        )

        VALUES (

            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s

        )
        """

        values = (

            event["city"],
            event["temperature_c"],
            event["humidity_percent"],
            event["wind_speed_kmh"],
            event["pressure_hpa"],
            event["event_time"],
            event["producer_timestamp"]

        )

        cursor.execute(query, values)

        connection.commit()

        logging.info("Weather Event Stored Successfully.")

    except Exception as e:

        connection.rollback()

        logging.error(f"Database Error : {e}")

def get_all_weather():
    """
    fetch all weather records from the database
    """        
    try:
        query="""
        SELECT*
        FROM weather_readings
        OEDER BY event_time DESC
        """

        cursor.execute(query)
        records=cursor.fetcall()
        return records
    except Exception as e:
        logging.error(
            f"Database Read Error: {e}"
        )
        return []
