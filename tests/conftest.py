import allure

def pytest_runtest_setup(item):
    # Автоматически добавляем label "layer" по pytest-маркерам
    if "api" in item.keywords:
        allure.dynamic.label("layer", "API Tests")
    if "ui" in item.keywords:
        allure.dynamic.label("layer", "UI Tests")
