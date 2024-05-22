#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage
from models.base_model import BaseModel
from models.city import City


class State(BaseModel):
    """ State class """
    name = ""

    @property
    def cities(self):
        """getter method that returns the list of city objects
        from storage linked to the current State"""
        from models import storage
        from models.city import City
        cities_list = []
        for city in storage.all(city).values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
