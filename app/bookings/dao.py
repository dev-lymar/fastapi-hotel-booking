from app.DAO.base import BaseDAO
from app.bookings.models import Bookings


class BookingDAO(BaseDAO):
    model = Bookings
