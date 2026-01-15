import allure


def pytest_runtest_setup(item):
    if "api" in item.keywords:
        allure.dynamic.label("layer", "api")

    if "ui" in item.keywords:
        allure.dynamic.label("layer", "UI")
