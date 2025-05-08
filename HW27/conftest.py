import json
import pytest


@pytest.fixture()
def read_config():
    with open("test_data/config.json") as f:
        return json.load(f)


@pytest.fixture()
def read_create_temp():
    with open("test_data/create_booking_temp.json") as f:
        return json.load(f)


@pytest.fixture()
def read_user_creds():
    with open("test_data/user_creds.json") as f:
        return json.load(f)

@pytest.fixture()
def read_partial_temp():
    with open("test_data/partial_update_temp.json") as f:
        return json.load(f)
