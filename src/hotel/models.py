from typing import Optional
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric, ForeignKey


class Hotels(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    location: Mapped[str] = mapped_column(String(200), nullable=True)
    rating: Mapped[float] = mapped_column(nullable=True)


class Rooms(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_number: Mapped[int] = mapped_column(nullable=True)
    floor: Mapped[int] = mapped_column(nullable=True)
    cost: Mapped[float] = mapped_column(Numeric(15, 2))
    employed: Mapped[bool] = mapped_column(default=False, nullable=True)
    number_beds: Mapped[int] = mapped_column(nullable=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"), nullable=False)