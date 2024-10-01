from confluent_kafka import Producer
import json
import os
import time


conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(conf)

start_latitude = 19.0760
start_longitude = 72.8777
end_latitude = 18.5294
end_longitude = 73.8567

steps = 1000

step_size_lat = (end_latitude - start_latitude) / steps
step_size_lon = (end_longitude - start_longitude) / steps
current_step = 0

def delivery_report(err, msg):
    if err is not None:
        print("message delivery failed: {err}")
    print(f"Message delivered to {msg.topic()} [{msg.partition()}], Value: {msg.value().decode('utf-8')}")

topic = "location_update"
while True:
    latitude = start_latitude + step_size_lat * current_step
    longitude = start_longitude + step_size_lon * current_step
    
    data = {
        'latitude' : latitude,
        'longitude' : longitude
    }
    
    producer.produce(topic, json.dumps(data).encode("utf-8"), callback=delivery_report)
    producer.flush()
    current_step += 1
    
    if current_step > steps:
        current_step = 0
    
    
    time.sleep(2)