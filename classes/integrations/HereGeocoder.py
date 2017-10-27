import classes.integrations
import config


class HereGeocoder(classes.integrations.BaseGeocoder.BaseGeocoder):

    host = 'geocoder.cit.api.here.com'
    basePath = '/6.2/'
    baseQuery = '?app_id=' + config.GeoPyRoxyConfig.HERE_APP_ID + '&app_code=' + config.GeoPyRoxyConfig.HERE_APP_CODE

    def __init__(self):
        super().__init__()

    def get_host(self):
        return self.host

    def get_reverse_geocode_url(self, coords):
        return self.basePath + 'reversegeocode.json' + self.baseQuery + '&searchtext='+coords

    def get_geocode_url(self, address):
        return self.basePath + 'geocode.json' + self.baseQuery + '&searchtext='+address #425+W+Randolph+Chicago
