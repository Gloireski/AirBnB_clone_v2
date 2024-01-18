#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    This class defines a user by various attributes

    Attributes:
        __tablename__ (str): the name of the Mysql table to store users.
        email (sqlalchemy string): user's mail adress
        password (sqlalchemy string): user's password
        first_name (sqlalchemy string): user's first name
        last_name (sqlalcheny string): user's last name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade="delete", backref="user")
