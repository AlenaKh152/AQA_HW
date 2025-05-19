import allure
from HW27.helper.send_request import send_request


# Тест позитивный: проверка получения списка всех бронирований
@allure.feature("Get booking(s)")
def test_01_get_all_bookings(read_config):
    URL = f'{read_config["URL"]}/booking'
    response = send_request("GET", URL)
    assert response
