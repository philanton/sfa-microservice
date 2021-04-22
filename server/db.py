import motor.motor_asyncio as async_motor
from typing import Optional

MONGO_DETAILS = "mongodb+srv://admin:1111@fcc.tcj3m.mongodb.net/sfa-models?retryWrites=true&w=majority"

db = async_motor.AsyncIOMotorClient(MONGO_DETAILS)

payment_collection = db.get_collection("payments")


async def add_payment(payment_data: dict) -> dict:
    payment = await payment_collection.insert_one(payment_data)
    return payment_data

async def get_payments(type: Optional[str] = None):
    query = {"type": type} if type else type
    payments = await payment_collection.find(query)
    return payments
