
import http.server
import io
import json
import shutil
import sys


class GeoHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def get_GEOCODE(self):
        return 'might be something'

    def get_REVERSE(self):
        return {"json": "might work"}

    def process_request(self):

        request_path = self.path.split('/')

        rest_method = self.command.lower()+'_'+request_path[1].upper()

        if not hasattr(self, rest_method):
            self.send_error(
                404,
                "Not Found (%r)" % rest_method)
        else:
            method = getattr(self, rest_method)
            return method()

        return ''

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
