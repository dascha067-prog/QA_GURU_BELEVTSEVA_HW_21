import allure


@allure.epic("Allure Examples")
@allure.feature("Basic pytest test")
@allure.story("Simple math validation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка вычитания двух чисел")
@allure.description(
    "Тест проверяет корректность операции вычитания. "
    "Используется для демонстрации шагов и severity в Allure."
)
def test_subtraction_of_two_numbers():
    with allure.step("Взять уменьшаемое = 10"):
        a = 10

    with allure.step("Взять вычитаемое = 4"):
        b = 4

    with allure.step("Вычесть второе число из первого"):
        result = a - b

    with allure.step("Проверить, что результат равен 6"):
        assert result == 6
