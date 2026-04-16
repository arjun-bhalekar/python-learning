import os

KAFKA_CONFIG = {
    'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVER','localhost:29092'),
    'group.id': os.getenv('KAFKA_GROUP_ID', 'order-consumer-group'),
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False
}

KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'orders')

DB_CONFIG = {
    "user": os.getenv('DB_USERNAME','martec'),
    "password": os.getenv('DB_PASSWORD','dev1234'),
    "dsn": os.getenv('DB_DSN','localhost:1521/FREEPDB1')
}