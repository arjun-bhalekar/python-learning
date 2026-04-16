import logging

from confluent_kafka import Consumer
import json

from config import KAFKA_CONFIG, KAFKA_TOPIC
from validator import validate_order
from db import insert_order

logger = logging.getLogger("consumer")


logger.info("Starting Kafka Consumer...")

consumer = Consumer(KAFKA_CONFIG)
consumer.subscribe([KAFKA_TOPIC])

logger.info(f"Listening to '{KAFKA_TOPIC}' topic...")

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            logger.error(f"Kafka Error: {msg.error()}")
            continue

        raw_message = msg.value().decode('utf-8')
        logger.info(f"message received :{raw_message}")

        try:
            order = json.loads(raw_message)

            validate_order(order)
            insert_order(order)
            consumer.commit()
            logger.info("message consumed & committed")

        except Exception as e:
            logger.error(f"Invalid message skipped: {e}")

except KeyboardInterrupt:
    logger.info("Stopping consumer...")

finally:
    consumer.close()