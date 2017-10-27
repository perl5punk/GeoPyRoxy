
import http.client


class SimpleHTTPClient:

    def __init__(self, host):
        self.host = host

    def get(self, url):

        try:

            http_connection = http.client.HTTPSConnection(self.host)
            http_connection.request("GET", url)
            response = http_connection.getresponse()
            data = response.read()

        except http.client.HTTPException as err:
            raise ValueError('HTTP Request Failed; '+err.args)

        return data
