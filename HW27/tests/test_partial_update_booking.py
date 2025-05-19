import allure
from HW27.helper.send_request import send_request


# Тест позитивный: частичное обновление бронирования
@allure.feature("Update booking")
def test_01_partial_upd_booking(read_config, read_user_creds, read_create_temp, read_partial_temp):
    URL = f'{read_config["URL"]}/booking'
    headers = {
        "Content-Type": "application/json"
    }
    booking_id = send_request("POST", URL, headers=headers, json=read_create_temp)["bookingid"]

    URL = f'{read_config["URL"]}/auth'
    token = send_request("POST", URL, json=read_user_creds)["token"]
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }
    URL = f'{read_config["URL"]}/booking/{booking_id}'
    response = send_request("PATCH", URL, headers=headers, json=read_partial_temp)
    assert response["firstname"] == read_partial_temp["firstname"]
    assert response["lastname"] == read_partial_temp["lastname"]
