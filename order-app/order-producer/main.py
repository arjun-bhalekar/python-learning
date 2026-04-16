from fastapi import FastAPI
from producer import send_order

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Order Producer Running"}

@app.post("/orders")
def create_order(order: dict):
    send_order(order)
    return {"status": "Order sent to Kafka", "order": order}