# Запуск тестов из Terminal:
# 1. Перейти в папку с тестом - ввести: cd tests
# 2. Команда запуска тестов:
# python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe test_cart_page.py
# """Тестируем корзину с книгами. 3 теста."""
import time

from pages.labirint_locators import MainPage


# """Тестируем, что выбранная книга добалена в корзину"""
def test_add_best_book_to_cart(web_browser):
    """ 1 Тестируем, что выбранная книга добалена в корзину"""
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    # Проверяем, что пользователь видит страницу с заголовком "Моя корзина":
    assert page.title_my_shopping_cart.get_text() == "Моя корзина: 1"
    # Проверяем, что на странице "Моя корзина" отображается добавленная в корзину книга:
    assert page.successfuly_odered.get_text() == "ВАШ ЗАКАЗ"


# """Добавляем книгу  и увеличиваем количество книг на 1 (2 книги в коризне)"""
def test_make_more_books_in_cart(web_browser):
    """ 2 Добавляем книгу  и увеличиваем количество книг на 1 (2 книги в коризне)"""
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    page.plus_one_more.click()
    time.sleep(5)
    # Проверяем, что на странице "Моя корзина" в счетчике отображается 2 книги:
    assert page.counter_selected_book.get_text() == "2 товара"


# """Добавляем и удаляем книгу в корзину (результат: пустая корзина)"""
def test_remove_book_from_cart(web_browser):
    """ 3 Добавляем и удаляем книгу в корзину (результат: пустая корзина)"""
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    page.remove_from_cart.click()
    # Проверяем, что на странице "Моя корзина" отображается "ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?":
    assert page.empty_cart.get_text() == "ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?"
