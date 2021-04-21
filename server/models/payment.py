from typing import Literal
from pydantic import BaseModel, Field


class PaymentSchema(BaseModel):
    type: Literal['Income', 'Outcome']
    total: int = Field(..., gt=0, lt=20000)

    class Config:
        schema_extra = {
            "example": {
                "type": "Income",
                "total": 3000
            }
        }
