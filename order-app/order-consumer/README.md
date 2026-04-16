# Kafka to Oracle Order Consumer

## Overview
Consumes order messages from Kafka and stores them in Oracle DB.

## Tech Stack
- Python
- Kafka
- Oracle DB
- Docker

## Architecture
Kafka → Python Consumer → Validation → Oracle

## How to Run

### 1. Start Kafka
docker-compose up -d

### 2. Build App
docker build -t order-consumer-app .

### 3. Run App
docker run -d --name order-consumer --network hip-net -e KAFKA_BOOTSTRAP_SERVER=kafka-server:9092 -e KAFKA_TOPIC=orders -e DB_USERNAME=martec -e DB_PASSWORD=dev1234 -e DB_DSN=oracle-db:1521/FREEPDB1 order-consumer-app:0.2

### 4. Send Message
kafka-console-producer ...