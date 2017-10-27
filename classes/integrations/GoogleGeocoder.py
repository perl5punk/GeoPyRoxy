import classes.integrations.BaseGeocoder
import config


class GoogleGeocoder(classes.integrations.BaseGeocoder.BaseGeocoder):

    host = 'maps.googleapis.com'
    baseUrl = '/maps/api/geocode/json?key=' + config.GeoPyRoxyConfig.GOOGLE_API_KEY

    def __init__(self):
        super().__init__()

    def get_host(self):
        return self.host

    def get_reverse_geocode_url(self, coords):
        return self.baseUrl + '&latlng=' + coords

    def get_geocode_url(self, address):
        return self.baseUrl + '&address=' + address
