from HW27.helper.send_request import send_request


# Тест позитивный: создание нового бронирования
def test_01_create_booking(read_config, read_create_temp):
    URL = f'{read_config["URL"]}/booking'
    headers = {
        "Content-Type": "application/json"
    }
    response = send_request("POST", URL, headers=headers, json=read_create_temp)
    assert response["booking"]["firstname"] == read_create_temp["firstname"]
    assert response["booking"]["lastname"] == read_create_temp["lastname"]
    assert response["booking"]["totalprice"] == read_create_temp["totalprice"]
    assert response["booking"]["depositpaid"] == read_create_temp["depositpaid"]
    assert (response["booking"]["bookingdates"]["checkin"] ==
            read_create_temp["bookingdates"]["checkin"])
    assert (response["booking"]["bookingdates"]["checkout"] ==
            read_create_temp["bookingdates"]["checkout"])
    assert response["booking"]["additionalneeds"] == read_create_temp["additionalneeds"]
