from typing import Dict
from pydantic import BaseModel, validator


class VehiclesParams(BaseModel):
    name: str
    cost: float
    capacity: float
    velocity: float
    local: str
    itinerary: Dict

    @validator('itinerary')
    def check_previous_receipt(cls, values):
        for key in values:
            if not isinstance(values.get(key), list):
                raise ValueError('O itinerário deve estar contigo dentro de uma lista com data e hora de saida e chegada.')
        return values
