# Запуск тестов из Terminal:
# 1. Перейти в папку с тестом - ввести: cd tests
# 2. Команда запуска тестов:
# python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe test_labirint.py
#'''Тест сайта labirint.ru. Главная страница 44 теста. '''

from pages.labirint import MainPage
import time


def test_check_main_search(web_browser):
    """_1 Проверка, что основной поиск работает нормально. """
    page = MainPage(web_browser)
    page.search = 'акулы'
    page.search_run_button.click()
    # Проверяем, что пользователь может видеть список книг:
    assert page.products_titles.count() == 60
    # Проверяем, что пользователь нашел соответствующие книги:
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'акул' in title.lower(), msg


def test_check_main_exact_search(web_browser):
    """_2 Проверка, что точный поиск работает нормально. """
    page = MainPage(web_browser)
    page.search = 'акулы из стали'
    page.search_run_button.click()
    # Проверяем, что пользователь может видеть список книг:
    assert page.products_titles.count() >= 1
    # Проверяем, что пользователь нашел соответствующие книги:
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'акулы из стали' in title.lower(), msg


def test_check_wrong_input_in_search(web_browser):
    """ 3 Проверка, что ввод с неправильной раскладки клавиатуры работает нормально. """
    page = MainPage(web_browser)
    # Попробуйте ввести «акулы» с английской клавиатуры:
    page.search = 'freks bp cnfkb'
    page.search_run_button.click()
    # Проверяем, что пользователь может видеть список книг:
    assert page.products_titles.count() >= 1
    # Проверяем, что пользователь нашел соответствующие книги:
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'акулы из стали' in title.lower(), msg


def test_check_wrong_input(web_browser):
    """ 4 Проверка, что поиск при вводе с орфографическими ошибками работает нормально. """
    page = MainPage(web_browser)
    # Попробуйте ввести «коромбол» с тремя ошибками:
    page.search = 'коромбол'
    page.search_run_button.click()
    # Проверяем, что пользователь может видеть список книг:
    assert page.products_titles.count() >= 1
    # Проверяем, что пользователь видит страницу с результатами поиска:
    title = page.page_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert title == 'Все, что мы нашли в Лабиринте по запросу «карамболь»', msg


def test_check_input_numbers_in_search(web_browser):
    """ 5 Проверка, что при вводе цифр поиск работает нормально, цифры в том числе переводятся в текст. """
    page = MainPage(web_browser)
    # Попробуйте ввести несколько цифр:
    page.search = '12'
    page.search_run_button.click()
    # Проверяем, что пользователь может видеть список товаров:
    assert page.products_titles.count() >= 1
    # Проверяем, что пользователь нашел соответствующие товары:
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert ('Двенадцать' in title, msg) or ('двенадцать' in title, msg) or ('12' in title, msg)


def test_check_input_symbols_in_search(web_browser):
    """ 6 Проверка, что при вводе знаков символов поиск работает нормально. """
    page = MainPage(web_browser)
    # Попробуйте ввести несколько знаков:
    page.search = '%!*'
    page.search_run_button.click()
    # Проверяем, что в списоке нет найденных товаров:
    assert page.products_titles.count() == 0
    # Проверяем, что появилось сообщение, что ничего не найдено:
    assert page.msg_search_er.get_text() == "Мы ничего не нашли по вашему запросу! Что делать?"


def test_check_search_electronic_books(web_browser):
    """ 7 Проверка, что поиск фильтром  электронных книг работает нормально. """
    page = MainPage(web_browser)
    page.search = 'мир'
    page.search_run_button.click()
    #time.sleep(5)
    # Убираем из результатов поиска другие товары, нажимаем на кнопку "Прочие товары":
    page.without_others_products_button.click()
    time.sleep(5)
    # Убираем из результатов поиска бумажные книги, нажимаем на кнопку "Бумажные книги":
    page.without_paper_books_button.click()
    time.sleep(5)
    # Проверяем, что пользователь может видеть список электронных книг:
    assert page.products_titles.count() >= 1
    assert page.products_titles.count() == 60
    # Проверяем, что найдены электронные книги:
    for title in page.products_types.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'электронная' in title.lower(), msg


def test_check_search_paper_books(web_browser):
    """ 8 Проверка, что поиск фильтр бумажных книг работает нормально. """
    page = MainPage(web_browser)
    page.search = 'мир'
    page.search_run_button.click()
    # Убираем из результатов поиска электронные книги, нажимаем на кнопку "Электронные книги":
    page.without_electronic_books_button.click()
    # Убираем из результатов поиска прочие товары, нажимаем на кнопку "Прочие товары":
    page.without_others_products_button.click()
    # Проверяем, что в найденных книгах нет электронных:
    for title in page.products_types.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'электронная' not in title.lower(), msg


def test_check_search_books(web_browser):
    """ 9 Проверка, что фильтр поиска только книг работает нормально. """
    page = MainPage(web_browser)
    page.search = 'дверь'
    page.search_run_button.click()
    # Убираем из результатов поиска другие товары, нажимаем на кнопку "Прочие товары":
    page.without_others_products_button.click()
    time.sleep(10)
    # Проверяем, что пользователь может видеть список именно книг:
    assert page.products_titles.count() >= 1
    assert page.products_titles.count() == 60


def test_check_search_expected(web_browser):
    """ 10 Проверка, что фильтр товаров со статусом "Ожидается" работает нормально. """
    page = MainPage(web_browser)
    page.search = 'золото'
    page.search_run_button.click()
    # Убираем из результатов поиска товары по предзаказу, нажимаем на кнопку "Предзаказ":
    page.sort_products_by_type_order.click()
    # Убираем из результатов поиска товары в наличии, нажимаем на кнопку "В наличии":
    page.sort_products_by_type_in_stock_is.click()
    # Проверяем, что в найденных книгах есть книги со статусом "ожидается":
    for title in page.products_waiting.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'ожидается' in title.lower(), msg


def test_check_search_in_stock(web_browser):
    """ 11 Проверка, что фильтр товаров "В наличии" работает нормально. """
    page = MainPage(web_browser)
    page.search = 'рюкзак'
    page.search_run_button.click()
    time.sleep(10)
    # Убираем из результатов поиска отсутствующие товары, нажимаем на кнопку "Нет в продаже":
    page.sort_products_by_type_out_of_stock.click()
    time.sleep(10)
    # Убираем из результатов поиска отсутствующие товары, нажимаем на кнопку "Ожидаются":
    page.sort_products_by_type_waiting.click()
    time.sleep(10)
    # Убираем из результатов поиска отсутствующие товары, нажимаем на кнопку "Предзаказ":
    page.sort_products_by_type_order.click()
    time.sleep(10)
    # Проверяем, что пользователь может видеть список товаров:
    assert page.products_titles.count() >= 1
    assert page.products_titles.count() == 60
    # Проверяем, что найдены товары, которые имеются в наличии, их можно положить в корзину:
    for title in page.products_in_stock.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'корзину' in title.lower(), msg


def test_check_search_electronic_books_another_way(web_browser):
    """ 12 Проверка, что фильтр электронных книг в выпадающем меню "ТИП ТОВАРА" работает нормально. """
    page = MainPage(web_browser)
    page.search = 'мир'
    page.search_run_button.click()
    # Нажимаем на кнопку "ТИП ТОВАРА":
    page.product_type.click()
    # Отжимаем галочку в строке "Бумажные книги":
    page.paper_books.click()
    # Отжимаем галочку в строке "Другие товары":
    page.other_goods.click()
    # Нажимаем на кнопку "Показать":
    page.show_button.click()
    time.sleep(10)
    # Проверяем, что найдены электронные книги:
    for title in page.products_types.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'электронная' in title.lower(), msg


def test_check_search_paper_books_another_way(web_browser):
    """ 13 Проверка, что фильтр бумажных книг в выпадающем меню "ТИП ТОВАРА" работает нормально. """
    page = MainPage(web_browser)
    page.search = 'мир'
    page.search_run_button.click()
    # Нажимаем на кнопку "ТИП ТОВАРА":
    page.product_type.click()
    # Отжимаем галочку в строке "Электронные книги":
    page.electronic_books.click()
    # Отжимаем галочку в строке "Другие товары":
    page.other_goods.click()
    # Нажимаем на кнопку "Показать":
    page.show_button.click()
    # Проверяем, что в найденных книгах нет электронных:
    for title in page.products_types.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'электронная' not in title.lower(), msg


def test_check_search_other_goods(web_browser):
    """ 14 Проверка, что фильтр других товаров в выпадающем меню "ТИП ТОВАРА" работает нормально. """
    page = MainPage(web_browser)
    page.search = 'рюкзак'
    page.search_run_button.click()
    # Нажимаем на кнопку "ТИП ТОВАРА":
    page.product_type.click()
    # Отжимаем галочку в строке "Бумажные книги":
    page.paper_books.click()
    page.show_button.scroll_to_element()
    # Нажимаем на кнопку "Показать":
    page.show_button.click()
    # Проверяем, что пользователь может видеть список товаров:
    assert page.products_titles.count() == 60


def test_check_search_best_buy_of_the_day(web_browser):
    """ 15 Проверка, что кнопка заголовок "Лучшая покупка дня" работает. """
    page = MainPage(web_browser)
    page.best_buy_of_the_day_button.click()
    # Проверяем, что пользователь может видеть список товаров "Лучшая покупка дня":
    assert page.products_best_buy_of_the_day.count() >= 1

def test_check_best_buy_of_the_day_button(web_browser):
    """ 16 Проверка, что кнопка заголовок "Лучшая покупка дня" ведет на нужную страницу. """
    page = MainPage(web_browser)
    page.best_buy_of_the_day_button.click()
    # Проверяем, что пользователь видит страницу с рекомендациями книг от редакции:
    title = page.discounts_today.get_text()
    # title = page.page_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'скидки сегодня' in title.lower(), msg


def test_check_search_what_to_read(web_browser):
    """ 17 Проверка, что кнопка заголовок "Что почитать: выбор редакции" работает. """
    page = MainPage(web_browser)
    page.what_to_read_button.click()
    # Проверяем, что пользователь может видеть список товаров:
    assert page.products_titles_large.count() >= 1

def test_check_button_what_to_read(web_browser):
    """ 18 Проверка, что кнопка "Что почитать: выбор редакции" ведет на нужную страницу. """
    page = MainPage(web_browser)
    page.what_to_read_button.click()
    # Проверяем, что пользователь видит страницу с заголовком
    # "Что почитать: выбор редакции" и рекомендациями книг от редакции:
    assert page.page_title.get_text() == "Что почитать: выбор редакции"


def test_check_actions_button(web_browser):
    """ 19 Проверка, что кнопка заголовок "Акции" ведет на нужную страницу. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку заголовок "Акции":
    page.actions_button.click()
    # time.sleep(5)
    # Проверяем, что пользователь видит страницу на которой есть подборка "Акции сентября":
    title = page.promo_month.get_text()
    # time.sleep(5)
    msg = 'Wrong product in search "{}"'.format(title)
    assert "акции сентября" in title.lower(), msg


def test_readers_choose_today(web_browser):
    """ 20 Проверка, что заголовок кнопка "Читатели выбирают сегодня" работает. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку "Читатели выбирают сегодня":
    page.button_readers_choose_today.click()
    # Проверяем, что пользователь может видеть список карточек книг "Читатели выбирают сегодня":
    assert page.books_cards_readers_choose_today.count() >= 1


def test_check_button_today(web_browser):
    """ 21 Проверка, что кнопка заголовок "Читатели выбирают сегодня" ведет на нужную страницу. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку "Читатели выбирают сегодня":
    page.button_readers_choose_today.click()
    # Проверяем, что пользователь видит страницу с заголовком "Главные книги":
    title = page.main_books.get_text()
    # title = page.page_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'главные книги' in title.lower(), msg


def test_check_button_labirint_now(web_browser):
    """ 22 Проверка, что кнопка "Лабиринт Сейчас — книжные события сентября" ведет на правильную страницу. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку "Лабиринт. Сейчас":
    page.labirint_now_button.click()
    # Проверяем, что пользователь видит нужную страницу:
    title = page.active_menu_item_labirint_now.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'лабиринт. сейчас' in title.lower(), msg
#
#
def test_check_сhild_navigator_button(web_browser):
    """ 23 Проверка, что кнопка заголовок "Детский навигатор — что читать детям и с детьми" ведет на правильную страницу. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку "Детский навигатор — что читать детям и с детьми":
    page.сhild_navigator_button.click()
    # Проверяем, что пользователь видит нужную страницу:
    title = page.active_menu_item_сhild_navigator.get_text()
    time.sleep(10)
    msg = 'Wrong product in search "{}"'.format(title)
    time.sleep(10)
    assert 'детский навигатор' in title.lower(), msg


def test_check_book_sales_leaders_button(web_browser):
    """ 24 Проверка, что кнопка "Книжные лидеры продаж" ведет на правильную страницу. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку "Книжные лидеры продаж":
    page.book_sales_leaders_button.click()
    # Проверяем, что пользователь видит нужную страницу:
    title = page.page_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    time.sleep(10)
    assert 'рейтинг продаж' in title.lower(), msg


def test_check_button_novelties_books(web_browser):
    """ 25 Проверка, что кнопка "Книги: новинки 2022" ведет на правильную страницу. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку заголовок "Книги: новинки 2022":
    page.novelties_books_button.click()
    # Проверяем, что пользователь видит нужную страницу:
    # title = page.page_title.get_text()
    title = page.novelties_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'новые книги' in title.lower(), msg


def test_check_button_reviews(web_browser):
    """ 26 Проверка, что кнопка "Книжные обзоры и рецензии" ведет на правильную страницу. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку "Книжные обзоры и рецензии":
    page.reviews_button.click()
    # Проверяем, что пользователь видит нужную страницу:
    title = page.heading_reviews.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'обзоры и рецензии' in title.lower(), msg


def test_check_button_delivery_and_payment(web_browser):
    """ 27 Проверка, что кнопка "Доставка и оплата" горизонтального меню ведет на правильную страницу. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку "Доставка и оплата":
    page.delivery_and_payment_button.click()
    # Проверяем, что пользователь видит нужную страницу:
    title = page.section_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'доставка' in title.lower(), msg


def test_check_button_certificates(web_browser):
    """ 28 Проверка, что кнопка "Сертификаты" горизонтального меню ведет на правильную страницу. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку "Сертификаты":
    page.certificates_button.click()
    # Проверяем, что пользователь видит нужную страницу:
    title = page.section_content.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'сертификаты' in title.lower(), msg


def test_check_button_ratings(web_browser):
    """ 29 Проверка, что кнопка "Рейтинги" горизонтального меню ведет на правильную страницу. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку "Рейтинги":
    page.ratings_button.click()
    # Проверяем, что пользователь видит нужную страницу:
    title = page.page_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'рейтинг' in title.lower(), msg


def test_check_new_product_button(web_browser):
    """ 30  Проверка, что кнопка "Новинки" горизонтального меню ведет на правильную страницу. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку "Новинки":
    page.new_product_button.click()
    # Проверяем, что пользователь видит нужную страницу:
    title = page.title_new_books.get_text()
    msg = 'Неправильный товар в поиске "{}"'.format(title)
    assert 'новые книги' in title.lower(), msg


def test_check_button_discounts(web_browser):
    """ 31 Проверка, что кнопка "Скидки" горизонтального меню ведет на правильную страницу. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку "Скидки":
    page.discounts_books_button.click()
    # Проверяем, что пользователь видит книги со скидками:
    for title in page.discounts_books.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert '%' in title, msg


def test_check_button_contacts(web_browser):
    """ 32 Проверка, что кнопка "Контакты" горизонтального меню ведет на правильную страницу. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку "Контакты":
    page.contacts_button.click()
    # Проверяем, что пользователь видит нужную страницу:
    title = page.page_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'контакты' in title.lower(), msg


def test_check_button_support(web_browser):
    """ 33 Проверка, что кнопка "Поддержка" горизонтального меню ведет на правильную страницу. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку "Поддержка":
    page.support_button.click()
    # Проверяем, что пользователь видит нужную страницу:
    title = page.section_title_support.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'публичные вопросы' in title.lower(), msg


def test_check_button_pickup_points(web_browser):
    """ 34 Проверка, что кнопка "507 (*в зависимости от региона) пункт самовывоза" горизонтального меню ведет на правильную страницу. """
    page = MainPage(web_browser)
    # Нажимаем на кнопку "N* пункт самовывоза":  ..._pickup_points
    page.pickup_points_button.click()
    # Проверяем, что пользователь видит нужную страницу:
    title = page.section_title_pickup_points.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'доставка' in title.lower(), msg


def test_check_search_authors(web_browser):
    """ 35 Проверка, что фильтр списка авторов по ключевому слову работает правильно. """
    page = MainPage(web_browser)
    page.search = 'зима'
    # time.sleep(5)
    page.search_run_button.click()
    # time.sleep(5)
    # Проверяем, что пользователь может видеть список книг:
    assert page.products_titles.count() == 60
    # time.sleep(5)
    # Нажимаем на кнопку "Авторы" в горизонтальном меню:
    page.authors_button.click()
    time.sleep(5)
    # Проверяем, что пользователь видит список авторов, отобранных по заданному параметру поиска:
    for title in page.authors_names.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'зима' in title.lower(), msg


def test_check_search_author(web_browser):
    """ 36 Проверка, что поиск страницы с книгами определенного автора работает правильно. """
    page = MainPage(web_browser)
    page.search = 'зима'
    page.search_run_button.click()
    # Нажимаем на кнопку "Авторы" в горизонтальном меню:
    page.authors_button.click()
    # Нажимаем на ФИО автора "Зима Владимир":
    page.our_author_button.click()
    # Проверяем, что пользователь видит страницу, посвященную искомому автору:
    title = page.page_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'зима владимир' in title.lower(), msg


def test_check_search_author_petrov(web_browser):
    """ 37 Проверка, что поиск книг определенного автора работает правильно. """
    page = MainPage(web_browser)
    page.search = 'ленин'
    page.search_run_button.click()
    # Нажимаем на кнопку "Авторы" в горизонтальном меню:
    page.authors_button.click()
    # Нажимаем на ФИО автора "ленин владимир ильич":
    page.lenin_author_button.click()
    # Проверяем, что пользователь видит страницу, посвященную искомому автору:
    title = page.page_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'ленин владимир ильич' in title.lower(), msg
    # Проверяем, что пользователь видит 28 книги:
    assert page.products_titles.count() == 28


def test_check_search_publishing_offices(web_browser):
    """ 38 Проверка, что фильтр списка книжных издательств по ключевому слову работает правильно. """
    page = MainPage(web_browser)
    page.search = 'золото'
    page.search_run_button.click()
    # Проверяем, что пользователь может видеть список книг:
    assert page.products_titles.count() == 60
    # Нажимаем на кнопку "Изд-ва" в горизонтальном меню:
    page.publishing_offices_button.click()
    # Проверяем, что пользователь видит список издательств, отобранных по заданному параметру поиска:
    for title in page.publishing_offices.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'золот' in title.lower(), msg

def test_check_search_publishing_office(web_browser):
    """ 39 Проверка, что поиск страницы с книгами определенного издательства работает правильно. """
    page = MainPage(web_browser)
    page.search = 'правда'
    page.search_run_button.click()
    # Нажимаем на кнопку "Изд-ва" в горизонтальном меню:
    page.publishing_offices_button.click()
    # Нажимаем на название издательства "Правда Севера":
    page.publishing_office_button.click()
    # Проверяем, что пользователь видит страницу, посвященную искомому издательству:
    title = page.page_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert title == '«Правда Севера»', msg


def test_check_search_author_golden_lion(web_browser):
    """ 40 Проверка, что поиск книг определенного издательства работает правильно. """
    page = MainPage(web_browser)
    page.search = 'правда'
    page.search_run_button.click()
    # Нажимаем на кнопку "Изд-ва" в горизонтальном меню:
    page.publishing_offices_button.click()
    # Нажимаем на название издательства "Правда Севера":
    page.publishing_office_button.click()
    # Нажимаем кнопку "Все книги" одного изд-ва:
    page.all_books_button_publishing_office.click()
    # Проверяем, что пользователь видит список книг:
    assert page.products_titles.count() >= 1


def test_check_search_product_series(web_browser):
    """ 41 Проверка, что фильтр списка серий товаров по ключевому слову работает правильно. """
    page = MainPage(web_browser)
    page.search = 'дворец'
    page.search_run_button.click()
    time.sleep(5)
    # Проверяем, что пользователь может видеть список книг:
    assert page.products_titles.count() == 60
    # Нажимаем на кнопку "Серии" в горизонтальном меню:
    page.product_series_button.click()
    # Проверяем, что пользователь видит список серий товаров, отобранных по заданному параметру поиска:
    for title in page.product_series.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'дворец' in title.lower() or 'дворц' in title.lower(), msg


def test_check_search_product_part(web_browser):
    """ 42 Проверка, что поиск страницы с товарами определенной серии работает правильно. """
    page = MainPage(web_browser)
    page.search = 'тайный'
    page.search_run_button.click()
    # Нажимаем на кнопку "Серии" в горизонтальном меню:
    page.product_series_button.click()
    # Нажимаем на название серии "Тайный город Вадима Панова Эксмо":
    page.series_selection_button.click()
    # Проверяем, что пользователь видит страницу c товарами искомой серии:
    # title = page.page_title.get_text()
    # title = page.tayniy_gorod.get_text()
    for title in page.tayniy_gorod.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'тайный город' in title.lower(), msg


def test_check_search_video(web_browser):
    """ 43 Проверка, что фильтр списка видео по ключевому слову работает правильно. """
    page = MainPage(web_browser)
    page.search = 'здоров'
    page.search_run_button.click()
    # Нажимаем на кнопку "Видео" в горизонтальном меню:
    page.video_button.click()
    # Проверяем, что пользователь может видеть список 25 видео, отобранных по заданному параметру поиска:
    assert page.video_products.count() == 31
    # проверяем, что в списке только названия видео со ссылками:
    for title in page.video_products.get_attribute('href'):
        msg = 'Wrong product in search "{}"'.format(title)
        assert title != '', msg

def test_check_search_themes(web_browser):
    """ 44 Проверка, что фильтр Темы по ключевому слову работает правильно. """
    page = MainPage(web_browser)
    page.search = 'кухня'
    page.search_run_button.click()
    # Нажимаем на кнопку "Темы" в горизонтальном меню:
    page.themes_button.click()
    # Проверяем, что пользователь может видеть список 6 тем, отобранных по заданному параметру поиска:
    assert page.themes_products.count() == 6
    # проверяем, что в списке названия тем со ссылками:
    for title in page.themes_products.get_attribute('href'):
        msg = 'Wrong product in search "{}"'.format(title)
        assert title != '', msg

