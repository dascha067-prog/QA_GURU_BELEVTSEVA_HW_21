import allure


@allure.epic("Allure Examples")
@allure.feature("Basic pytest test")
@allure.story("Division rules")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка деления без остатка")
@allure.description(
    "Тест проверяет, что деление выполняется корректно, "
    "если делитель не равен нулю."
)
def test_division_without_remainder():
    with allure.step("Взять делимое = 8"):
        a = 8

    with allure.step("Взять делитель = 2"):
        b = 2

    with allure.step("Разделить делимое на делитель"):
        result = a / b

    with allure.step("Проверить, что результат равен 4"):
        assert result == 4
