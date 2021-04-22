from fastapi import FastAPI
from typing import Optional
from server.models.payment import PaymentSchema

app = FastAPI()


@app.post("/save", tags=["payment"])
async def save_payment(payment: PaymentSchema):
    print(payment)

@app.get("/stats", tags=["payment"])
async def get_stats(type: Optional[str] = None):
    pass
