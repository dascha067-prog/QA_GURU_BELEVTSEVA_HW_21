import allure
import pytest
import requests


BASE_URL = "https://petstore.swagger.io/v2"


@allure.epic("Allure Examples")
@allure.feature("API")
@allure.story("Swagger Petstore")
@allure.tag("api")
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API: Получение питомца по id")
@allure.description(
    "Тест проверяет, что Swagger Petstore возвращает данные питомца по существующему id. "
    "Используется как простой и стабильный пример API-теста."
)
def test_get_pet_by_id():
    pet_id = 1
    url = f"{BASE_URL}/pet/{pet_id}"

    with allure.step(f"Отправить GET запрос на {url}"):
        response = requests.get(url, timeout=10)

    with allure.step("Проверить, что статус-код равен 200"):
        assert response.status_code == 200

    with allure.step("Проверить, что в ответе есть поле id"):
        response_json = response.json()
        assert "id" in response_json
        assert response_json["id"] == pet_id

    with allure.step("Приложить тело ответа в Allure"):
        allure.attach(
            str(response_json),
            name="response_body",
            attachment_type=allure.attachment_type.JSON
        )
