from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder

from typing import Optional
import asyncio
from server.auth.auth_bearer import JWTBearer
from server.auth.auth_handler import signJWT

from server.models.payment import PaymentSchema
import server.db as db

app = FastAPI()


@app.post("/save", dependencies=[Depends(JWTBearer())], tags=["payment"])
async def save_payment(payment: PaymentSchema):
    payment_data = jsonable_encoder(payment)
    res = await db.add_payment(payment_data)
    return payment

@app.get("/stats", dependencies=[Depends(JWTBearer())], tags=["payment"])
async def get_stats(type: Optional[str] = None):
    payments = [p['total'] for p in await db.get_payments(type)]
    avg = sum(payments) / len(payments)
    return avg

@app.post("/token", tags=["token"])
async def get_token(username: str):
    return signJWT(username)


@app.get("/", tags=["main"])
async def get_main():
    return {"message": "Welcome to Seriy-Phil-Anton API!"}
