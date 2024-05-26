from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI()


class HotelsSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


class SHotel(BaseModel):
    addres: str
    name: str
    stars: int


@app.get("/hotels")
def get_hotels(
    search_args: HotelsSearchArgs = Depends()
) -> list[SHotel]:
    hotels = [
        {
            'address': 'Zelena, 6',
            'name': 'Top byt',
            'stars': 5,
        }
    ]
    return search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking: SBooking):
    pass