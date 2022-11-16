# Запуск тестов из Terminal:
# 1. Перейти в папку с тестом - ввести: cd tests
# 2. Команда запуска тестов:
# python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe test_auth_page.py
# """Тестируем возможность входа  в личный кабинет с корректным и некорректным логином (код скидки). 4 теста."""

from pages.labirint_locators import MainPage
import time


# """Вход с корретными данными авторизации(код скидки)"""
def test_valid_login_auth_page(web_browser):
    """ 1 Вход с корретными данными авторизации"""
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("AE9A-43EE-BECB")
    page.enter_button.click()
    time.sleep(6)
    page.my_labirint.click()
    # Проверяем, что пользователь видит страницу с заголовком: "Личный кабинет —"
    assert page.page_title_cabinet.get_text() == "Личный кабинет —"


# """Вход с некорретными данными авторизации(код скидки)"""
def test_invalid_login_auth_page(web_browser):
    """ 2 Вход с некорретными данными авторизации"""
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("12F8-41C9-80DB")
    page.enter_button.click()

    title = page.auth_error.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert title == 'Введенного кода не существует', msg


# """Вход с пустым полем ввода авторизации"""
def test_blanc_login_auth_page(web_browser):
    """ 3 Вход с пустым полем ввода авторизации"""
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("      ")

    title = page.auth_error_2.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert title == 'Нельзя использовать символ « »', msg


# """Вход с корретными данными авторизации(по электронной почте)"""
def test_email_login_auth_page(web_browser):
    """ 4 Вход с корретными данными авторизации(по электронной почте)"""
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("bula03@yandex.ru")
    page.enter_button.click()
    page.login_field.send_keys("AE9A-43EE-BECB")
    page.check_code_and_enter_button.click()
    time.sleep(6)
    page.my_labirint.click()
    # Проверяем, что пользователь видит страницу с заголовком: "Личный кабинет —"
    assert page.page_title_cabinet.get_text() == "Личный кабинет —"
