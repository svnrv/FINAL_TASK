# Запуск тестов из Terminal:
# 1. Перейти в папку с тестом - ввести: cd tests
# 2. Команда запуска тестов:
# python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe test_book_page.py
# """Тестируем книги с главной страницы. 4 теста."""

from pages.labirint_locators import MainPage


# """Тестируем, что выбранная книга добалена в корзину"""
def test_add_best_book_to_cart(web_browser):
    """ 1 Тестируем, что выбранная книга добалена в корзину"""
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    # Проверяем, что на странице "Моя корзина" отображается добавленная в корзину книга:
    assert page.successfuly_odered.get_text() == "ВАШ ЗАКАЗ"


# """Тестируем, что выбранная книга добалена в отложенные"""
def test_add_best_book_to_deferred(web_browser):
    """ 2 Тестируем, что выбранная книга добалена в отложенные"""
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.add_to_deferred.click()
    page.deferred.click()
    # Проверяем, что пользователь видит страницу "Отложенные товары":
    assert page.deferred_items.get_text() == "Отложенные товары 1"
    # Проверяем, что пользователь может видеть список отложенных товаров:
    assert page.products_deferred.count() >= 1


# """Тестируем, что выбранная книга добалена к сравнению"""
def test_add_best_book_to_comparison(web_browser):
    """ 3 Тестируем, что выбранная книга добалена к сравнению"""
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.add_to_compare_button.click()
    page.compare_button.click()
    # Проверяем, что пользователь видит страницу "Сравнение товаров":
    assert page.title_product_compare.get_text() == "Сравнение товаров"


# """Тестируем сравнение книг"""
def test_compare_books(web_browser):
    """ 4 Тестируем сравнение книг"""
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.add_to_compare_button.click()
    page.logo_labirint.click()
    page.best_sale.click()
    page.random_book_1.click()
    page.add_to_compare_button.click()
    page.compare_button.click()
    # Проверяем, что пользователь видит страницу "Сравнение товаров":
    assert page.get_current_url() == 'https://www.labirint.ru/compare/'
