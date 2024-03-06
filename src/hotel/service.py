from typing import Optional
from pydantic import TypeAdapter
from src.hotel.repository import HotelsRepository
from src.hotel.schemas import HotelSchema


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