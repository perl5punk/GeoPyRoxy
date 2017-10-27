
from abc import ABCMeta, abstractmethod

import classes.interfaces.http


class BaseGeocoder:
    __metaclass__ = ABCMeta

    host = 'localhost'

    def __init__(self):
        self.http_client = classes.interfaces.http.SimpleHTTPClient(self.get_host())

    def coords_from_address(self, address):
        print('hit coords_from_address in BASE with '+address)
        return self.http_client.get(self.get_geocode_url(address))

    def address_from_coords(self, coords):
        print('hit address_from_coords in BASE with '+coords)
        return self.http_client.get(self.get_reverse_geocode_url(coords))

    @abstractmethod
    def get_host(self):
        return self.host

    @abstractmethod
    def get_geocode_url(self, address):
        return address

    @abstractmethod
    def get_reverse_geocode_url(self, coords):
        return coords
