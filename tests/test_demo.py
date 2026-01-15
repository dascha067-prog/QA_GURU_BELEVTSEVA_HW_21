import allure
import pytest


@pytest.mark.ui
@allure.epic("Allure Examples")
@allure.feature("Basic pytest test")
@allure.story("Simple math validation")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка сложения двух чисел")
@allure.description(
    "Тест проверяет, что операция сложения работает корректно. "
    "Используется как пример тестовой документации в Allure."
)
def test_sum_of_two_numbers():
    with allure.step("Взять первое число = 2"):
        a = 2

    with allure.step("Взять второе число = 3"):
        b = 3

    with allure.step("Сложить числа"):
        result = a + b

    with allure.step("Проверить, что результат равен 5"):
        assert result == 5
