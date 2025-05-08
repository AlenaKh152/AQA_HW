import requests
import pytest
from helper.send_request import send_request


# Тест позитивный: получение бронирования по id
def test_01_get_booking_by_id(read_config, read_user_creds, read_create_temp):
    URL = f"{read_config["URL"]}/booking"
    headers = {
        "Content-Type": "application/json"
    }
    booking_id = send_request("POST", URL, headers=headers, json=read_create_temp)["bookingid"]

    URL = f"{read_config["URL"]}/booking/{booking_id}"
    response = send_request("GET", URL)
    assert response["firstname"] == read_create_temp["firstname"]
    assert response["lastname"] == read_create_temp["lastname"]
    assert response["totalprice"] == read_create_temp["totalprice"]
    assert response["depositpaid"] == read_create_temp["depositpaid"]
    assert response["bookingdates"]["checkin"] == read_create_temp["bookingdates"]["checkin"]
    assert response["bookingdates"]["checkout"] == read_create_temp["bookingdates"]["checkout"]
    assert response["additionalneeds"] == read_create_temp["additionalneeds"]


# Тест негативный: получение несуществующего бронирования по id
def test_02_get_unknown_booking_by_id(read_config, read_user_creds, read_create_temp):
    URL = f'{read_config["URL"]}/booking'
    headers = {
        "Content-Type": "application/json"
    }
    booking_id = send_request("POST", URL, headers=headers, json=read_create_temp)["bookingid"]

    URL = f'{read_config["URL"]}/auth'
    token = send_request("POST", URL, json=read_user_creds)["token"]

    URL = f'{read_config["URL"]}/booking/{booking_id}'
    headers = {
        "Cookie": f"token={token}"
    }
    requests.delete(URL, headers=headers) # Удаляем бронирование
    response = requests.get(URL)
    assert response.status_code == 404 # Проверяем, что бронирование не найдено
