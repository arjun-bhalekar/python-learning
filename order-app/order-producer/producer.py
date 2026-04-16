from confluent_kafka import Producer
import json
from config import KAFKA_CONFIG, KAFKA_TOPIC

producer = Producer(KAFKA_CONFIG)

def delivery_report(err, msg):
    if err:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} on {msg.partition()} with offset {msg.offset()}")

def send_order(order):
    producer.produce(
        KAFKA_TOPIC,
        value=json.dumps(order),
        callback=delivery_report
    )
    producer.flush()