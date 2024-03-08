import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.hotel.repository import HotelsRepository, RoomsRepository
from src.hotel.schemas import HotelSchema, RoomSchema
from src.db import Base, engine

from src.hotel.service import HotelsService, RoomsService
# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)


print(" Hotels ".center(80, "="))

hotel_1 = HotelSchema(name="Hotelleon", location="Moscow", rating="4.98")
added_hotel = HotelsService.add(hotel_1)
all = HotelsService.list()
first = HotelsService.get(36)
print(f"{added_hotel=}")
print()
print(f"{all=}")
print()
print(f"{first=}")

print()
print()

print(" Rooms ".center(80, "="))

room_1 = RoomSchema(room_number="4345", floor="32", cost="20000,00", employed=False, number_beds="1", hotel_id="1")
added_room = RoomsService.add(room_1)
all = RoomsService.list()
first = RoomsService.get(36)
print(f"{added_room=}")
print()
print(f"{all=}")
print()
print(f"{first=}")