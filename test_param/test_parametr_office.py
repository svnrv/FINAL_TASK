# Запуск тестов из Terminal:
# 1. Перейти в папку с тестом, ввести: cd test_param
# 2. Запуск теста, файл chromedriver.exe лежит в папке: test_param\chrome\chromedriver.exe
#    команда запуска:
# python -m pytest -v --driver Chrome --driver-path test_param\chrome\chromedriver.exe test_parametr_office.py

""" Тест ссылок раздела 'Канцелярские товары' сайта labirint.ru с использованием параметризации"""

import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def python_string_slicer(driver, str):
    # time.sleep(10)
    element = driver.find_elements(By.XPATH, str)[0]
    return element


def setUpClass(cls):
    cls.service = Service()
    cls.driver = webdriver.Chrome(service=cls.service)
    cls.driver.implicitly_wait(10)
    cls.driver.maximize_window()


@pytest.fixture(scope="function", params=[
    ('//a[@href="/genres/2300/"]', "/genres/2300/"),
    ('//a[@href="/genres/1500/"]', "/genres/1500/"),
    ('//a[@href="/genres/2646/"]', "/genres/2646/"),
    ('//a[@href="/genres/1444/"]', "/genres/1444/"),
    ('//a[@href="/genres/1367/"]', "/genres/1367/"),
    ('//a[@href="/genres/1321/"]', "/genres/1321/"),
    ('//a[@href="/genres/1394/"]', "/genres/1394/"),
    ('//a[@href="/genres/1405/"]', "/genres/1405/"),
    ('//a[@href="/genres/2752/"]', "/genres/2752/"),
    ('//a[@href="/genres/1496/"]', "/genres/1496/")
], ids=["1.Аксесуары для книг",
        "2.Глобусы",
        "3.Обложки для документов",
        "4.Офисная канцелярия",
        "5.Папки, скоросшиватели, разделители",
        "6.Письменные принадлежности",
        "7.Принадлежности для черчения",
        "8.Рисование",
        "9.Сумки",
        "10.Товары для школы"
        ])
def param_fun(request):
    return request.param


def test_labirint_office(param_fun):
    (input, expected_output) = param_fun
    driver = webdriver.Chrome(r"C:/chromedriver/chromedriver.exe")
    driver.get('https://www.labirint.ru/office/')

    input_coocie = '//button[@class="cookie-policy__button js-cookie-policy-agree"]'  # Закрываем окно о куках, нажатием кнопки "Принять"
    coocie_click = python_string_slicer(driver, input_coocie)
    coocie_click.click()

    result = python_string_slicer(driver, input)
    time.sleep(10)

    result.click()
    time.sleep(10)
    assert ('https://www.labirint.ru' + expected_output) == driver.current_url
    driver.close()
