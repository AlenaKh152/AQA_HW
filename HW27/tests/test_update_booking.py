import requests
import pytest
from helper.send_request import send_request


# Тест позитивный: обновление бронирования
def test_01_update_booking(read_config, read_create_temp, read_user_creds):
    URL = f"{read_config["URL"]}/booking"
    headers = {
        "Content-Type" : "application/json"
    }

    booking_id = send_request(
        "POST", URL, headers=headers, json=read_create_temp)["bookingid"] # Создаем бронирование

    URL = f"{read_config["URL"]}/auth"

    token = send_request("POST", URL, json=read_user_creds)["token"]
    URL = f'{read_config["URL"]}/booking/{booking_id}'
    headers = {
        "Content-Type" : "application/json",
        "Cookie" : f"token={token}"
    }
    read_create_temp["firstname"] = "Ammy"
    read_create_temp["lastname"] = "Day"
    response = send_request(
        "PUT", URL, headers=headers, json=read_create_temp ) # Обновляем бронирование
    assert response["firstname"] == read_create_temp["firstname"]
    assert response["lastname"] == read_create_temp["lastname"]


# Тест негативный: обновление несуществующего бронирования
def test_02_update_unknown_booking(read_config, read_create_temp, read_user_creds):
    URL = f"{read_config["URL"]}/booking"
    headers = {
        "Content-Type" : "application/json"
    }
    booking_id = send_request(
        "POST", URL, headers=headers, json=read_create_temp)["bookingid"] # Создаем бронирование
    URL = f"{read_config["URL"]}/auth"
    token = send_request("POST", URL, json=read_user_creds)["token"]

    URL = f'{read_config["URL"]}/booking/{booking_id}'
    headers = {
        "Cookie": f"token={token}"
    }
    requests.delete(URL, headers=headers) # Удаляем бронирование

    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }
    read_create_temp["firstname"] = "Ammy"
    read_create_temp["lastname"] = "Day"
    response = requests.put(URL, headers=headers, json=read_create_temp) # Обновляем бронирование
    assert response.status_code == 405  # Проверяем, что обновление бронирования не доступно
