import requests
import logging
import os
import sys


class DistanceAPIClient(object):

    def __init__(self):
        self.url = self.set_api_url()
        self.session = requests.Session()
        self.session.headers = {
            "authentication": "key={0}".format(os.environ['API_KEY']),
            "Accept": "application/json"
            }

        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        logging.getLogger("requests").setLevel(logging.ERROR)
        self.log = logging.getLogger(__name__)

    def set_api_url(self, output="json"):
        return "https://maps.googleapis.com/maps/api/distancematrix/{0}".format(output)

    def assert_code(self, response, expected_code):
        try:
            assert response.status_code == expected_code
        except AssertionError:
            self.log.info("RESPONSE: {0}".format(response.text.encode("utf-8")))
            raise

    def get_distance(self, data, expected_code=200):
        resp = self.session.get(self.url, params=data)
        self.assert_code(resp, expected_code)
        return resp