import pytest
import undetected_chromedriver as uc
import warnings


@pytest.fixture()
def browser():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    options = uc.ChromeOptions()
    options.add_argument("--password-store=basic")
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )
    options.add_argument("--headless")
    driver = uc.Chrome(options=options)

    yield driver  # Возвращаем браузер для использования в тестах
    driver.quit()
