import motor.motor_asyncio as async_motor
from typing import Optional

from server.config import USERNAME, PASSWORD

MONGO_DETAILS = "mongodb+srv://{}:{}@fcc.tcj3m.mongodb.net/sfa-models?retryWrites=true&w=majority".format(USERNAME, PASSWORD)

client = async_motor.AsyncIOMotorClient(MONGO_DETAILS)
db = client["sfa-models"]
payment_collection = db.get_collection("payments")


async def add_payment(payment_data: dict) -> dict:
    payment = await payment_collection.insert_one(payment_data)
    return payment_data

async def get_payments(type: Optional[str] = None):
    query = {"type": type} if type else type
    payments = await payment_collection.find(query).to_list(length=100)
    return payments
