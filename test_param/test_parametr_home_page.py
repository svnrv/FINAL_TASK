# Запуск тестов из Terminal:
# 1. Перейти в папку с тестом, ввести: cd test_param
# 2. Запуск теста, файл chromedriver.exe лежит в папке: test_param\chrome\chromedriver.exe
#    команда запуска:
# python -m pytest -v --driver Chrome --driver-path test_param\chrome\chromedriver.exe test_parametr_home_page.py

'''Тестирование кнопок в шапке главной страницы сайта lsbirint.ru'''

import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# -*-coding:utf-8-*-

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
    ('//*[@class="b-header-b-logo-e-logo-wrap"]', '/'),
    ('//*[@class="b-header-b-personal-e-link top-link-main top-link-main_putorder"]', '/cabinet/putorder/'),
    ('//*[@class="b-header-b-personal-e-list-item have-dropdown  last-child"]', '/cart/'),
    ('//*[@class="b-header-e-icon-adult b-header-e-icon-adult-m-big b-header-e-sprite-background"]', '/agreement/'),
    ('//span[@class="b-header-b-menu-e-link top-link-menu first-child"]', '/books/'),
    ('//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[2]/span/a', '/best/'),
    ('//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div[1]/div[1]/ul[1]/li[3]/span[1]/a[1]', '/school/'),
    ('//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div[1]/div[1]/ul[1]/li[4]/span[1]/a[1]', '/games/'),
    ('//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div[1]/div[1]/ul[1]/li[5]/span[1]/a[1]', '/office/'),
    ('//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[11]/span/a', '/club/'),
    ('//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[1]/a', '/help/'),
    ('//*[@id="minwidth"]/div[5]/div[1]/div[2]/div[1]/ul[1]/li[2]/a[1]', '/top/certificates/'),
    ('//a[@href="/rating/?id_genre=-1&nrd=1"]', '/rating/?id_genre=-1&nrd=1'),
    ('//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[4]/a', '/novelty/'),
    ('//a[@href="/sale/"]', '/search/?discount=1&available=1&order=actd&way=back&paperbooks=1&ebooks=1&otherbooks=1'),
    ('//*[@data-event-content="Контакты"]', '/contact/'),
    ('//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[10]/a', '/support/'),
    ('//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[11]/a', '/maps/')
],
                ids=[
                    "1_logo",
                    "2_deferred",
                    "3_cart",
                    "4_plus_18",
                    "5_header_books",
                    "6_header_main_2022",
                    "7_header_school",
                    "8_header_toys",
                    "9_header_office",
                    "10_header_club",
                    "11_delivery_and_payment",
                    "12_certificates",
                    "13_rating",
                    "14_new_books",
                    "15_discount",
                    "16_contacts",
                    "17_support",
                    "18_maps"
                ])
def param_fun(request):
    return request.param


def test_home_page(param_fun):
    (input, expected_output) = param_fun
    driver = webdriver.Chrome(r"C:/chromedriver/chromedriver.exe")
    driver.get('https://www.labirint.ru/')

    input_coocie = '//button[@class="cookie-policy__button js-cookie-policy-agree"]'  # Закрываем окно о куках, нажатием кнопки "Принять"
    coocie_click = python_string_slicer(driver, input_coocie)
    coocie_click.click()
    driver.maximize_window()
    result = python_string_slicer(driver, input)
    # time.sleep(10)
    print(result)
    result.click()
    # time.sleep(10)
    assert ('https://www.labirint.ru' + expected_output) == driver.current_url
    driver.close()
