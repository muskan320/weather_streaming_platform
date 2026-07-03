from kafka import KafkaProducer   #import kafka producer

#import json module
import json  

#import kafka server and topic name from config file
from configs.kafka_config import(
    BOOTSTRAP_SERVER,
    RAW_TOPIC
)

#CREATE KAFKA PRODUCER
producer=KafkaProducer(

    #kafka server address
    bootstrap_servers=BOOTSTRAP_SERVER,

    #convert python data to json and then to bytes
    value_serializer=lambda value:
    json.dumps(value).encode("utf-8")

)


#function to send event to kafka topic
def publish_event(event,key=None):
    future=producer.send(

        #topic where data will be send
        #we have created topic in kafka_config.py
        topic=RAW_TOPIC,

        #It is the optional message key
        key=key.encode("utf-8") if key else None,

        #event data
        value=event
    )

    #return send status
    return future


#function to send event and wait for confirmation
def publish_and_confirmation(event,key=None):
    future=publish_event(event,key)

    #wait for kafka confirmation(10 sec)
    metadata=future.get(timeout=10)

    #return message
    return metadata

def close():
    producer.flush()
    producer.close()

