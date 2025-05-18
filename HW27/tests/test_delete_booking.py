import requests
from HW27.helper.send_request import send_request


# Тест позитивный: удаление бронирования по id
def test_01_delete_booking(read_config, read_user_creds, read_create_temp):
    URL = f'{read_config["URL"]}/booking'
    headers = {
        "Content-Type": "application/json"
    }
    booking_id = send_request(
        "POST", URL, headers=headers, json=read_create_temp)["bookingid"]  # Создаем бронирование

    URL = f'{read_config["URL"]}/auth'
    token = send_request("POST", URL, json=read_user_creds)["token"]

    URL = f'{read_config["URL"]}/booking/{booking_id}'
    headers = {
        "Cookie": f"token={token}"
    }
    response = requests.delete(URL, headers=headers)  # Удаляем бронирование
    assert response.status_code == 201  # Проверяем, что бронирование удалено
    response = requests.get(URL)
    assert response.status_code == 404  # Проверяем, что бронирование не найдено


# Тест негативный: удаление несуществующего бронирования
def test_02_delete_unknown_booking(read_config, read_user_creds, read_create_temp):
    URL = f'{read_config["URL"]}/booking'
    headers = {
        "Content-Type": "application/json"
    }
    booking_id = send_request(
        "POST", URL, headers=headers, json=read_create_temp)["bookingid"]  # Создаем бронирование

    URL = f'{read_config["URL"]}/auth'
    token = send_request("POST", URL, json=read_user_creds)["token"]

    URL = f'{read_config["URL"]}/booking/{booking_id}'
    headers = {
        "Cookie": f"token={token}"
    }
    requests.delete(URL, headers=headers)  # Удаляем бронирование
    response = requests.delete(URL, headers=headers)  # Повторно удаляем бронирование
    assert response.status_code == 405   # Проверяем запрет на повторное удаление
