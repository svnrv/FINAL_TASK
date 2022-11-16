# Запуск тестов из Terminal:
# 1. Перейти в папку с тестом - ввести: cd tests
# 2. Команда запуска тестов:
# python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe test_search_page.py
# """Тестируем поиск по тексту с главной страницы. 6 тестов."""

import time
from pages.labirint_locators import MainPage


# """Тестируем поиск с корректным названием"""
def test_successful_search(web_browser):
    """ 1 Тестируем поиск с корректным названием"""
    page = MainPage(web_browser)
    page.search.send_keys('Гнев всемогущий')
    page.search_btn.click()

    assert page.successful_search.get_text() == "Все, что мы нашли в Лабиринте по запросу «Гнев всемогущий»"


# """Тестируем поиск - название кириллицей вводится латиницей"""
def test_successful_latinica(web_browser):
    """ 2 Тестируем поиск - название кириллицей вводится латиницей"""
    page = MainPage(web_browser)
    page.search.send_keys('Gnev vsemgushchy')
    page.search_btn.click()

    assert page.not_successful_search.get_text() == "Мы ничего не нашли по вашему запросу! Что делать?"


# """Тестируем поиск - по цифрам поиск работает"""
def test_successful_numbers(web_browser):
    """ 3 Тестируем поиск по цифрам"""
    page = MainPage(web_browser)
    page.search.send_keys('123456')
    page.search_btn.click()

    assert page.successful_search.get_text() == "Все, что мы нашли в Лабиринте по запросу «123456»"


# """Тестируем поиск по пробелам"""
def test_not_successful_blanc(web_browser):
    """ 4 Тестируем поиск по пробелам"""
    page = MainPage(web_browser)
    page.search.send_keys('           ')
    page.search_btn.click()

    assert page.not_successful_search.get_text() == "Мы ничего не нашли по вашему запросу! Что делать?"


# """Тестируем поиск по случайным символам"""
def test_not_successful_search_random(web_browser):
    """ 5 Тестируем поиск по случайным символам"""
    page = MainPage(web_browser)
    page.search.send_keys('!@#$%^&*()')
    page.search_btn.click()

    assert page.not_successful_search.get_text() == "Мы ничего не нашли по вашему запросу! Что делать?"


# """Тестируем поиск по тексту с главной страницы с применением фильтров - в наличии"""
def test_only_available(web_browser):
    """ 6 Тестируем поиск по тексту с главной страницы с применением фильтров - в наличии"""
    page = MainPage(web_browser)
    page.search.send_keys('акулы из стали')
    page.search_btn.click()
    page.all_filers_button.click()
    page.reset_all_filers.click()
    page.available.click()
    page.show_all_found_button.click()
    # Проверяем, что пользователь нашел соответствующие книги:
    for title in page.available_products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'акул' in title.lower(), msg
    assert page.available_products_titles.count() == 5
