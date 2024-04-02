from typing import Optional
from pydantic import TypeAdapter
from src.hotel.repository import HotelsRepository, RoomsRepository
from src.hotel.schemas import HotelSchema, RoomSchema


class HotelsService:
    @classmethod
    def add(cls, hotel: HotelSchema):
        hotel_dict = hotel.to_dict_wo_id()
        new_hotel = HotelsRepository.add(hotel_dict)
        return TypeAdapter(HotelSchema).dump_python(new_hotel)

    @classmethod
    def get(cls, hotel_id: int):
        hotel = HotelsRepository.get(hotel_id)
        return TypeAdapter(HotelSchema).dump_python(hotel)

    @classmethod
    def list(
            cls,
            name: Optional[str] = None,
            location: Optional[str] = None,
            rating: Optional[float] = None,
    ):
        filter_by = {k: v for k, v in {"name": name, "location": location, "rating": rating}.items() if v}
        candies = HotelsRepository.list(filter_by)
        return TypeAdapter(list[HotelSchema]).dump_python(candies)

    @classmethod
    def count(cls) -> int:
        count = HotelsRepository.count()
        return count

    @classmethod
    def update(cls, hotel_id: int, hotel: HotelSchema):
        hotel_dict = hotel.to_dict_wo_id()
        HotelsRepository.update(hotel_id, hotel_dict)

    @classmethod
    def delete(cls, hotel_id: int):
        HotelsRepository.delete(hotel_id)

    @classmethod
    def delete_all(cls):
        HotelsRepository.delete_all()


class RoomsService:
    @classmethod
    def add(cls, room: RoomSchema):
        room_dict = room.to_dict_wo_id()
        new_room = RoomsRepository.add(room_dict)
        return TypeAdapter(RoomSchema).dump_python(new_room)

    @classmethod
    def get(cls, room_id: int):
        room = RoomsRepository.get(room_id)
        return TypeAdapter(RoomSchema).dump_python(room)

    @classmethod
    def list(
            cls,
            room_number: Optional[str] = None,
            floor: Optional[str] = None,
            cost: Optional[str] = None,
            employed: Optional[str] = None,
            number_beds: Optional[str] = None
    ):
        filter_by = {k: v for k, v in {"room_number": room_number, "floor": floor, "cost": cost, "employed": employed, "number_beds": number_beds}.items() if v}
        rooms = RoomsRepository.list(filter_by)
        return TypeAdapter(list[RoomSchema]).dump_python(rooms)

    @classmethod
    def count(cls) -> int:
        count = RoomsRepository.count()
        return count

    @classmethod
    def update(cls, room_id: int, room: RoomSchema):
        room_dict = room.to_dict_wo_id()
        RoomsRepository.update(room_id, room_dict)

    @classmethod
    def delete(cls, room_id: int):
        RoomsRepository.delete(room_id)

    @classmethod
    def delete_all(cls):
        RoomsRepository.delete_all()