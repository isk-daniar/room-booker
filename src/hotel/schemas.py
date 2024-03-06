from typing import Optional
from pydantic import BaseModel, Field


class HotelSchema(BaseModel):
    id: Optional[int] = Field(default=1)
    name: str
    location: str
    rating: float



    class Config:
        from_attributes = True

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        for attr in ["name", "location", "rating"]:
            if getattr(self, attr) != getattr(other, attr):
                return False
        return True

    def to_dict_wo_id(self) -> dict:
        return self.model_dump(exclude={"id"})


class RoomSchema(BaseModel):
    id: Optional[int] = Field(default=1)
    room_number: int
    floor: int
    cost: float
    employed: bool = Field(default=False)
    number_beds: int



    class Config:
        from_attributes = True

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        for attr in ["room_number", "floor", "cost", "employed", "number_beds"]:
            if getattr(self, attr) != getattr(other, attr):
                return False
        return True

    def to_dict_wo_id(self) -> dict:
        return self.model_dump(exclude={"id"})