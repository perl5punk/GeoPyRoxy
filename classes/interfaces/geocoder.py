
import importlib


class GeocoderServiceInterface:

    services = {}

    def __init__(self, service_order):
        self.service_order = service_order
        for service in self.service_order:
            try:
                pkgimport = importlib.import_module("classes.integrations."+service)
                _init_class = getattr(pkgimport, service)
                self.services[service] = _init_class()
                print('loaded '+service)
            except ValueError as e:
                print("Failed to load: "+service+' service package. ')

    def process_geocode_request(self, type, path):
        for name, service in self.services.items():
            try:
                if hasattr(service, type):
                    service_method = getattr(service, type)
                    print('calling '+name+'->'+type+' with '+str(path))
                    return service_method(path.pop())
                    break

            except Exception as e:
                raise ValueError('Failed while making geocode request; '+e.args)

        return 'Request failed, ' + type + ' not found'
