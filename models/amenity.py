#!/usr/bin/python3
""" Amenty Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amnety class definition
    Attributes:
        __tablename__: table to store amneties
        name: name of amenty
        place_amenities: place related
    """
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
