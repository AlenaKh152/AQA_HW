from helper.send_request import send_request


# Тест позитивный: проверка получения списка всех бронирований
def test_01_get_all_bookings(read_config):
    URL = f'{read_config["URL"]}/booking'
    response = send_request("GET", URL)
    assert response


# Тест позитивный: проверка получения бронирования по имени
def test_02_get_all_bookings_by_name(read_config, read_create_temp):
    URL = f'{read_config["URL"]}/booking'
    headers = {
        "Content-Type": "application/json"
    }
    read_create_temp["firstname"] = "Testbookingname"
    response = send_request("POST", URL, headers=headers, json=read_create_temp)

    firstname = response["booking"]["firstname"]  # Имя в новом бронировании
    booking_id = response["bookingid"]  # Id нового бронирования

    URL = f'{read_config["URL"]}/booking?firstname={firstname}'  # Поиск по имени
    response = send_request("GET", URL)
    assert response[0]["bookingid"] == booking_id
