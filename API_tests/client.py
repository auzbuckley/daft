import requests
import logging
import os
import sys


class DistanceAPIClient(object):

    def __init__(self):
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        logging.getLogger("requests").setLevel(logging.ERROR)
        self.log = logging.getLogger(__name__)

        self.base_url = "https://maps.googleapis.com/maps/api/distancematrix/"
        self.session = requests.Session()
        self.session.headers = {
            "authentication": "key={0}".format(os.environ['API_KEY']),
            "Accept": "application/json"
            }

    def get_url(self, output):
        url = self.base_url + output
        self.log.debug("URL: {0}".format(url))
        return url

    def get_distance(self, data, output="json", expected_code=200):
        resp = self.session.get(self.get_url(output=output), params=data)
        self._assert_code(resp, expected_code)
        return resp

    def _assert_code(self, response, expected_code):
        try:
            assert response.status_code == expected_code
        except AssertionError:
            self.log.info("RESPONSE: {0}".format(response.text.encode("utf-8")))
            raise
