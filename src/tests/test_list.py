import pytest

from config import settings
from db import Base, engine
from hotel.schemas import HotelSchema
from hotel.service import HotelsService


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    print(f"{settings.DB_NAME=}")
    assert settings.MODE == "TEST"
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@pytest.fixture()
def hotels():
    hotels = [
        HotelSchema(name="LeionHotel", location="SPB", rating="4.2"),
        HotelSchema(name="StarHotel", location="Moscow", rating='2.5'),
        HotelSchema(name="MoonHotel", location="Ufa", rating='5.0'),
    ]
    return hotels


@pytest.fixture(scope="function")
def empty_hotels():
    HotelsService.delete_all()


@pytest.mark.usefixtures("empty_hotels")
class TestHotel:
    def test_count_hotel(self, hotels):
        for hotel in hotels:
            HotelsService.add(hotel)

        assert HotelsService.count() == 3

    def test_list_hotel(self, hotels):
        for hotel in hotels:
            HotelsService.add(hotel)

        all_hotels = HotelsService.list()
        for added_hotel in all_hotels:
            assert added_hotel in hotels
