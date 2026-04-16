import os

KAFKA_CONFIG = {
    'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVER','localhost:29092'),
}

KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'orders')