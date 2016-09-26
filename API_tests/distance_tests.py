# -*- coding: utf-8 -*-

import pytest
import requests
from client import DistanceAPIClient
import logging


class TestDirectionsAPI(object):

    def setup(self):
        self.client = DistanceAPIClient()
        self.log = logging.getLogger(__name__)

    def test_optional_parameters_only(self):
        data = {
            "mode": "bicycling"
        }
        resp = self.client.get_distance(data)
        assert resp.json()["status"] == "INVALID_REQUEST"

    def test_required_parameters_only(self):
        data = {
            "origins": "Vancouver BC|Seattle",
            "destinations": "San Francisco|Victoria BC"
        }
        resp = self.client.get_distance(data)
        assert resp.json()["status"] == "OK"
        origins = ["Vancouver, BC, Canada", "Seattle, WA, USA"]
        assert all(x in resp.json()["origin_addresses"] for x in origins)

    def test_partial_required_parameters(self):
        data = {
            "origins": "Vancouver BC"
        }
        resp = self.client.get_distance(data)
        assert resp.json()["status"] == "INVALID_REQUEST"

    def test_required_parameters_and_optional_parameters(self):
        data = {
            "origins": "Vancouver BC|Seattle",
            "destinations": "San Francisco|Victoria BC",
            "language": "fr"
        }
        resp = self.client.get_distance(data)
        assert resp.json()["status"] == "OK"
        french = "San Francisco, Californie, États-Unis"
        assert french.decode("utf-8") in resp.json()["destination_addresses"]

    def test_no_supported_language(self):
        data = {
            "origins": "Vancouver BC|Seattle",
            "destinations": "San Francisco|Victoria BC",
            "language": "xx"
        }
        resp = self.client.get_distance(data)
        assert resp.json()["status"] == "OK"
        english = "San Francisco, CA, USA"
        assert english in resp.json()["destination_addresses"]

    def test_no_output_specified(self):
        self.client.url = self.client.set_api_url(output=None)
        data = {
            "origins": "Vancouver BC|Seattle",
            "destinations": "San Francisco|Victoria BC",
            "mode": "bicycling"
        }
        resp = self.client.get_distance(data, 404)
        self.client.url = self.client.set_api_url()
