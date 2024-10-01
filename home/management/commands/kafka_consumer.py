from confluent_kafka import Consumer, KafkaException, KafkaError
from django.core.management.base import BaseCommand
import json
from home.models import LocationUpdate

class Command(BaseCommand):
    help = "Run kafka consumer to listen location update"
    def handle(self, *args, **options):
        conf = {
                    'bootstrap.servers': 'localhost:9092',
                    'group.id': 'location_update_live_location',
                    'auto.offset.reset' : 'earliest',
                    'enable.partition.eof' : "true",
                }
        
        consumer = Consumer(conf)
        consumer.subscribe(['location_update'])
        try:
            while True:
                msg = consumer.poll(timeout = 1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # print("End of partition reached")
                        continue
                    else:
                        print(f"Error: {msg.error()}")
                        break
                
                # Add a check to ensure the message is not empty
                message_value = msg.value().decode("utf-8")
                if not message_value.strip():  # Check for empty message
                    print("Received empty message, skipping...")
                    continue

                data = json.loads(msg.value().decode("utf-8"))
                LocationUpdate.objects.create(
                    latitude = data['latitude'],
                    longitude = data['longitude']
                )
                print(f"recieved and saved : {data}")
        
        except KeyboardInterrupt:
            pass
        finally:
            consumer.close()
        # return super().handle(*args, **options)


