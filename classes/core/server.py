
import http.server
import io
import json
import shutil
import sys

import classes.interfaces.geocoder
import config


class GeoHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    geocoder = classes.interfaces.geocoder.GeocoderServiceInterface(config.GeoPyRoxyConfig.PREFERRED_SERVICE_ORDER)

    def get_GEOCODE(self, path):
        return self.geocoder.process_geocode_request('coords_from_address', path)

    def get_REVERSE(self, path):
        return self.geocoder.process_geocode_request('address_from_coords', path)

    def process_request(self):

        request_response = ''
        request_path = self.path.split('/')
        rest_method = self.command.lower()+'_'+request_path[1].upper()

        if not hasattr(self, rest_method):
            self.send_error(
                404,
                "Not Found (%r)" % rest_method)
        else:
            try:
                method = getattr(self, rest_method)
                print('calling '+rest_method)
                request_response = method(request_path)
            except ValueError as e:
                request_response = format(str(e))

        return request_response

    def do_GET(self):

        enc = sys.getfilesystemencoding()
        data = self.process_request()
        content_type = 'text/plain'

        if type(data) is dict:
            data = json.dumps(data)
            content_type = 'application/json'

        encoded = ('\n\n'+data).encode(enc, 'surrogateescape')

        self.send_response(200)
        self.send_header("Content-type", content_type+"; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()

        f = io.BytesIO()
        f.write(encoded)
        f.seek(0)

        if f:
            try:
                shutil.copyfileobj(f, self.wfile)
            finally:
                f.close()
