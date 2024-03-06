from sqlalchemy import delete, func, insert, select, update
from src.db import Session

from src.hotel.models import Hotels, Rooms


class HotelsRepository:
    @classmethod
    def add(cls, values: dict):
        with Session() as session:
            stmt = insert(Hotels).values(**values).returning(Hotels)
            new_hotel = session.execute(stmt)
            session.commit()
            return new_hotel.scalar_one()

    @classmethod
    def get(cls, hotel_id: int):
        query = select(Hotels.__table__.columns).filter_by(id=hotel_id)
        with Session() as session:
            hotel = session.execute(query)
            session.commit()
            return hotel.mappings().one()

    @classmethod
    def list(cls, filter_by: dict):
        query = select(Hotels).filter_by(**filter_by)
        with Session() as session:
            hotels = session.execute(query)
            session.commit()
            return hotels.scalars().all()

    @classmethod
    def count(cls) -> int:
        query = select(func.count(Hotels.id)).select_from(Hotels)
        with Session() as session:
            hotels_count = session.execute(query)
            session.commit()
            return hotels_count.scalar()

    @classmethod
    def update(cls, hotel_id: int, values: dict):
        stmt = update(Hotels).where(Hotels.id == hotel_id).values(**values)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def finish(cls, hotel_id: int, values: dict):
        stmt = update(Hotels).where(Hotels.id == hotel_id).values(**values)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def delete(cls, hotel_id: int):
        stmt = delete(Hotels).where(Hotels.id == hotel_id)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def delete_all(cls):
        stmt = delete(Hotels)
        with Session() as session:
            session.execute(stmt)
            session.commit()


class RoomsRepository:
    @classmethod
    def add(cls, values: dict):
        with Session() as session:
            stmt = insert(Rooms).values(**values).returning(Rooms)
            new_room = session.execute(stmt)
            session.commit()
            return new_room.scalar_one()

    @classmethod
    def get(cls, room_id: int):
        query = select(Rooms.__table__.columns).filter_by(id=room_id)
        with Session() as session:
            room = session.execute(query)
            session.commit()
            return room.mappings().one()

    @classmethod
    def list(cls, filter_by: dict):
        query = select(Rooms).filter_by(**filter_by)
        with Session() as session:
            rooms = session.execute(query)
            session.commit()
            return rooms.scalars().all()

    @classmethod
    def count(cls) -> int:
        query = select(func.count(Rooms.id)).select_from(Rooms)
        with Session() as session:
            rooms_count = session.execute(query)
            session.commit()
            return rooms_count.scalar()

    @classmethod
    def update(cls, room_id: int, values: dict):
        stmt = update(Rooms).where(Rooms.id == room_id).values(**values)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def finish(cls, room_id: int, values: dict):
        stmt = update(Rooms).where(Rooms.id == room_id).values(**values)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def delete(cls, room_id: int):
        stmt = delete(Rooms).where(Rooms.id == room_id)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def delete_all(cls):
        stmt = delete(Rooms)
        with Session() as session:
            session.execute(stmt)
            session.commit()