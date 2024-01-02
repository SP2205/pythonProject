import requests
import pytest


def test_CreateBooking_positive():
    print("Create booking testcases")
    URL= "https://restful-booker.herokuapp.com/booking"
    requests.post(URL)
