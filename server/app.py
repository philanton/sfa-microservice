from fastapi import FastAPI
from server.models.payment import PaymentSchema

app = FastAPI()


@app.post("/save", tags=["payment"])
async def read_root(payment: PaymentSchema):
    return payment
