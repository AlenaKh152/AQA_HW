import requests
import pytest
from helper.send_request import send_request


# Тест позитивный: получение токена
def test_01_get_token(read_config, read_user_creds):
    URL = f'{read_config["URL"]}/auth'
    headers = {
        "Content-Type" : "application/json"
    }
    token = send_request("POST", URL, headers=headers, json=read_user_creds)["token"]
    assert token


# Тест негативный: получение токена по неизвестным username и password
def test_02_get_token_by_wrong_creds(read_config, read_user_creds):
    URL = f'{read_config["URL"]}/auth'
    headers = {
        "Content-Type" : "application/json"
    }
    read_user_creds["username"] = "unknown_user_name"
    read_user_creds["password"] = "unknown_user_password"
    response = send_request("POST", URL, headers=headers, json=read_user_creds)
    assert response["reason"] == "Bad credentials"
