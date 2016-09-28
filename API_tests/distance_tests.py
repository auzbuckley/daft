# -*- coding: utf-8 -*-

import pytest
import requests
from client import DistanceAPIClient
import logging


class TestDistanceAPI(object):
    
    def setup(self):
        self.client = DistanceAPIClient()
        self.log = logging.getLogger(__name__)

    def test_multiple_origins_and_destinations_returns_correct_results(self):
        data = {
            "origins": "Wellington|Rotorua",
            "destinations": "Auckland|Wanganui",
        }
        resp = self.client.get_distance(data)
        assert resp.json()["status"] == "OK"

        origins = ["Wellington, New Zealand", "Rotorua, New Zealand"]
        assert all(origin in resp.json()["origin_addresses"] for origin in origins)

        destinations = ["Auckland, New Zealand", "Whanganui, New Zealand"]
        assert all(destination in resp.json()["destination_addresses"] for destination in destinations)

        rows = self._get_result_rows(resp)
        assert len(rows) == 2  # check there are two rows

        self._check_result_elements(rows)

    def test_no_required_parameters_returns_invalid_request(self):
        data = {
            "mode": "bicycling"
        }
        resp = self.client.get_distance(data)
        assert resp.json()["status"] == "INVALID_REQUEST"

    def test_single_required_parameter_only(self):
        data = {
            "origins": "Dublin"
        }
        resp = self.client.get_distance(data)
        assert resp.json()["status"] == "INVALID_REQUEST"

    def test_no_output_specified_returns_404(self):
        data = {
            "origins": "Limerick",
            "destinations": "Galway",
            "mode": "bicycling"
        }
        self.client.get_distance(data, output="", expected_code=404)

    def test_results_returned_in_specified_language(self):
        data = {
            "origins": "Limerick",
            "destinations": "Galway",
            "language": "fr"
        }
        resp = self.client.get_distance(data)
        assert resp.json()["status"] == "OK"

        french = "Galway, Irlande"
        assert french.decode("utf-8") in resp.json()["destination_addresses"]

    def test_results_returned_in_default_language(self):
        data = {
            "origins": "Limerick",
            "destinations": "Galway",
            "language": "xx"
        }
        resp = self.client.get_distance(data)
        assert resp.json()["status"] == "OK"

        english = "Galway, Ireland"
        assert english in resp.json()["destination_addresses"]
        
    def _get_result_rows(self, resp):
        return resp.json()["rows"]

    def _check_result_elements(self, rows):
        for row in rows:
            elements = row["elements"]
            assert len(elements) == 2  # check there are two elements within each row 
            self._check_element_details(elements)

    def _check_element_details(self, elements):
        for element in elements:
            assert element["status"] == "OK"  # check the status for each element is OK

            duration_value = element["duration"]["value"]
            assert isinstance(duration_value, int) and duration_value > 0  # check duration value is an integer and above zero

            distance_value = element["distance"]["value"]
            assert isinstance(distance_value, int) and duration_value > 0  # check distance value is an integer and above zero
