import os
from pages.base import WebPage
from pages.elementes import WebElement
from pages.elementes import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    # поле основного поиска на главной странице
    search = WebElement(id='search-field')
    # кнопка основного поиска
    search_run_button = WebElement(xpath='//button[@type="submit"]')
    # названия книг в результатах поиска на главной странице
    products_titles = ManyWebElements(xpath='//a[@class="product-title-link"]')

    # заголовок страницы на странице "Что почитать: выбор редакции"
    page_title = WebElement(xpath='//h1')

    # сообщение об ошибке поиска на главной странице
    msg_search_er = WebElement(xpath='//h1')


    # кнопка отключения "Прочие товары" в результатах поиска
    without_others_products_button = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Прочие")]')
    # кнопка отключения "Бумажные книги" в результатах поиска
    without_paper_books_button = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Бумажные")]')
    # по результату фильтрации в карточках книг "тип товара"
    products_types = ManyWebElements(xpath='//span[@class="card-label__text card-label__text_inversed"]')

    # кнопка отключения "Электронные книги" в результатах поиска
    without_electronic_books_button = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Электронные")]')

    # кнопка "Предзаказ" в результатах поиска
    sort_products_by_type_order = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Предзаказ")]')
    # кнопка "В наличии" в результатах поиска
    sort_products_by_type_in_stock_is = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"В наличии")]')
    # по результату поиска в описании товара статус "Ожидается"
    products_waiting = ManyWebElements(xpath='//a[@class="btn-not-avaliable"]')

    # кнопка "Нет в продаже" в результатах поиска
    sort_products_by_type_out_of_stock = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Нет в продаже")]')
    # кнопка "Ожидаются" в результатах поиска
    sort_products_by_type_waiting = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Ожидаются")]')
    # часть описания товара, где расположена надпись "В корзину"
    products_in_stock = ManyWebElements(
        xpath='//div[@class="btn buy-link btn-primary"]')

    # кнопка ТИП ТОВАРА в результатах поиска "мир"
    product_type = WebElement(xpath='//span[@class="navisort-item__content" and contains(text(),"ТИП ТОВАРА")]')
    # в кнопке ТИП ТОВАРА в выпадающем списке  - строка Бумажные книги
    paper_books = WebElement(xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"Бумажные")]')
    # в кнопке ТИП ТОВАРА в выпадающем списке - строка Другие товары
    other_goods = WebElement(xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"Другие")]')
    # в кнопке ТИП ТОВАРА в выпадающем списке кнопка "Показать"
    show_button = WebElement(xpath='//input[@class="w100p show-goods__button" and @value="Показать"]')


    # кнопка ТИП ТОВАРА в выпадающем списке - строка Электронные книги
    electronic_books = WebElement(
        xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"Электронные")]')

    # на главной странице кнопка "Что почитать: выбор редакции"
    what_to_read_button = WebElement(xpath='//a[@class="block-link-title"][text()="Что почитать: выбор редакции"]')
    # названия книг на странице "Что почитать: выбор редакции"
    products_titles_large = ManyWebElements(xpath='//span[@class="product-title large-name"]')

    # на главной странице кнопка "Новинки"
    new_product_button = WebElement(xpath='//a[@class="b-header-b-sec-menu-e-link"][text()="Новинки"]')
    # содержание раздела на открывшейся странице "Новинки"
    title_new_books = WebElement(xpath='//h1[text()="Новые книги"]')

    # на главной странице заголовок кнопка "Лучшая покупка дня"
    best_buy_of_the_day_button = WebElement(xpath='//a[text()="Лучшая покупка дня"]')
    # названия книг на странице "Лучшая покупка дня"
    products_best_buy_of_the_day = ManyWebElements(xpath='//a[@class="product-title-link"]')

    # заголовок кнопка "скидки сегодня" на странице "Главные книги 2022"
    discounts_today = WebElement(xpath='//a[text()="Скидки сегодня"]')

    # на главной странице кнопка заголовок "Акции"
    actions_button = WebElement(xpath='//a[@class="block-link-title"][text()="Акции"]')

    # на странице Акции "Лучшая покупка дня" карточки книг со скидками
    #action_label_space = ManyWebElements(xpath='//span[@class="card-label__text card-label__text_turned"]')
    action_label_space = ManyWebElements(xpath='//a[contains(@class, "card-label card-label_turned")]')

    # на странице "Акции" кнопка заголовок Акции сентября
    promo_month = WebElement(xpath='//h1[@class="actions__title"][text()="Акции сентября"]')

    # кнопка "Читатели выбирают сегодня"
    button_readers_choose_today = WebElement(xpath='//a[@class="block-link-title"][text()="Читатели выбирают сегодня"]')
    # карточки книг "Читатели выбирают сегодня"
    books_cards_readers_choose_today = ManyWebElements(xpath='// div[@class ="jcarousel-item book-item need-watch watched"]')

    # кнопка заголовок "Главные книги 2022"
    main_books = WebElement(xpath='//h1[text()="Главные книги 2022"]')

    # # карточки электронных бумажных книг в результатах поиска
    # products_books = ManyWebElements(
    #     xpath='//div[@class="product need-watch watched" and @data-dir="books"]')

    # кнопка заголовок "Лабиринт. Сейчас — книжные события сентября"
    labirint_now_button = WebElement(
        xpath='//a[@class="block-link-title"][text()="Лабиринт. Сейчас — книжные события сентября"]')
    # активный пункт горизонтального меню, который соответсвует содержанию открывшейся страницы
    active_menu_item_labirint_now = WebElement(
        xpath='//a[@class="mm-link mm-link-big mm-link-big-m-sub active"]')

    # кнопка заголовок "Детский навигатор — что читать детям и с детьми"
    #сhild_navigator_button = WebElement(xpath='//a[@class="block-link-title"][text()="Детский навигатор — что читать детям и с детьми"]')
    сhild_navigator_button = WebElement(xpath='//a[@class="block-link-title"][text()="Детский навигатор — что читать детям и с детьми"]')
    # активный пункт горизонтального меню, который соответсвует содержанию открывшейся страницы
    active_menu_item_сhild_navigator = WebElement(
        xpath='//a[@class="mm-link mm-link-big mm-link-big-m-sub active"]')

    # кнопка "Книги для школы"
    books_for_school_button = WebElement(xpath='//a[@class="block-link-title"][text()="Книги для школы"]')

    # кнопка заголовок "Книжные лидеры продаж"
    book_sales_leaders_button = WebElement(
        xpath='//a[@class="block-link-title"][text()="Книжные лидеры продаж"]')

    # кнопка заголовок "Книги: новинки 2022"
    novelties_books_button = WebElement(
        xpath='//a[@class="block-link-title"][text()="Книги: новинки 2022"]')
    # заголовок "Новые книги" на открывшейся странице
    novelties_title = WebElement(xpath='//h1[text()="Новые книги"]')

    # кнопка заголовок "Книжные обзоры и рецензии"
    reviews_button = WebElement(
        xpath='//a[@class="block-link-title"][text()="Книжные обзоры и рецензии"]')
    # заголовок на открывшейся странице "Книжные обзоры и рецензии"
    heading_reviews = WebElement(
        xpath='//div[@class="ratingh h1"][text()="Книжные обзоры и рецензии"]')

    # кнопка "Доставка и оплата"
    delivery_and_payment_button = WebElement(
        xpath='//a[@class="b-header-b-sec-menu-e-link"][text()="Доставка и оплата"]')
    # название раздела на странице "Доставка и оплата"
    section_title = WebElement(xpath='//a[text()="Доставка"]')

    # кнопка "Сертификаты" в горизонтальном меню
    certificates_button = WebElement(
        xpath='//a[@class="b-header-b-sec-menu-e-link"][text()="Сертификаты"]')
    # содержание раздела на открывшейся странице "Сертификаты"
    section_content = WebElement(
        xpath='//div[@class="b-subscribetext-title"][text()="Подарочные сертификаты"]')

    # кнопка "Рейтинги" в горизонтальном меню
    ratings_button = WebElement(
        xpath='//a[@class="b-header-b-sec-menu-e-link"][text()="Рейтинги"]')

    # кнопка "Скидки" в горизонтальном меню
    discounts_books_button = WebElement(
        xpath='//a[@class="b-header-b-sec-menu-e-link"][text()="Скидки"]')
    # описание скидки на книгу в результатах поиска "Больше книг со скидками"
    discounts_books = ManyWebElements(
        xpath='//a[contains(@class, "card-label_profit")]')

    # кнопка "Контакты" в горизонтальном меню
    contacts_button = WebElement(
        xpath='//a[@class="b-header-b-sec-menu-e-link"][text()="Контакты"]')

    # кнопка "Контакты" в горизонтальном меню
    support_button = WebElement(
        xpath='//a[@class="b-header-b-sec-menu-e-link"][text()="Поддержка"]')
    # название раздела на странице "Поддержка"
    section_title_support = WebElement(xpath='//a[@class="support-all active"]')

    # кнопка "пункт самовывоза" в горизонтальном меню
    pickup_points_button = WebElement(
        xpath='//a[@href="/maps/"][@class="b-header-b-sec-menu-e-link"]')
    # название раздела на странице "пункт самовывоза"
    section_title_pickup_points = WebElement(
        xpath='//span[@class="delivery-map-wrapper__header-text-inline"][text()="Доставка"]')

    # кнопка "Авторы" в горизонтальном меню
    authors_button = WebElement(xpath='//span[text()="Авторы"]')
    # список авторов в результатах поиска
    authors_names = ManyWebElements(xpath='//a[@class="rubric-list-item"]')

    # кнопка выбора автора "Зима Владимир"
    our_author_button = WebElement(
        xpath='//a[@class="rubric-list-item"][@href="/authors/32719/"]')

    # кнопка выбора автора "Ленин Владимир Ильич"
    lenin_author_button = WebElement(
        xpath='//a[@class="rubric-list-item"][@href="/authors/49043/"]')

    # кнопка "Изд-ва" в горизонтальном меню
    publishing_offices_button = WebElement(
        xpath='//a[@class="b-stab-e-slider-item-e-txt js-search-result-tab"][@data-id_tab="2"]')
    # список издательств в результатах поиска
    publishing_offices = ManyWebElements(
        xpath='//a[@class="rubric-list-item"]')

    # кнопка выбора издательста "Правда Севера"
    publishing_office_button = WebElement(
        xpath='//span[@class="rubric-item-name"][contains(text(), "Правда Севера")]')

    # кнопка "Все книги" одного издательства
    all_books_button_publishing_office = WebElement(
        xpath='//a[@data-page="/pubhouse/books/1800/"][@data-notonavi="1"]')

    # кнопка "Серии" в горизонтальном меню
    product_series_button = WebElement(
        xpath='//a[@class="b-stab-e-slider-item-e-txt js-search-result-tab"][@data-id_tab="4"]')
    # список серий товаров в результатах поиска
    product_series = ManyWebElements(
        xpath='//a[@class="rubric-list-item"]')

    # кнопка выбора серии "Тайный город Вадима Панова Эксмо"
    series_selection_button = WebElement(
        xpath='//span[@class="rubric-item-name"][contains(text(), "Тайный город Вадима")]')
    # содержание раздела на открывшейся странице "Тайный город Вадима Панова Эксмо"
    tayniy_gorod = WebElement(xpath='//h1[text()="Серия «Тайный город Вадима Панова»"]')

    # кнопка 'вид "таблицей"'в результатах поиска тайный город
    view_table = WebElement(xpath='//*[@id="catalog-navigation"]/form[1]/div[1]/div[1]/div[1]/div[1]/span[3]/span[1]/a[2]')
    # названия книг в результатах поиска тайный город
    products_titles1 = ManyWebElements(xpath='//a[@class="book-qtip"]')

    # кнопка "Видео" в горизонтальном меню
    video_button = WebElement(
        xpath='//a[@class="b-stab-e-slider-item-e-txt js-search-result-tab"][@data-id_tab="17"]')
    # список видео в результатах поиска
    video_products = ManyWebElements(
        xpath='//a[@class="rubric-list-item videobloc-carousel-item js-videoblock-video-show"]')

    # кнопка "Темы" в горизонтальном меню
    themes_button = WebElement(
        xpath='//a[@class="b-stab-e-slider-item-e-txt js-search-result-tab"][@data-id_tab="12"]')
    # список тем в результатах поиска
    themes_products = ManyWebElements(xpath='//span[@class="rubric-item-name"]')

    # кнопка "Мамин борщ и бабушкины пироги. Рецепты счастливой кухни от Маши Трауб"
    theme_button = WebElement(
        xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a[1]/span')
    # содержание раздела на открывшейся странице "Мамин борщ и бабушкины пироги. Рецепты счастливой кухни от Маши Трауб"
    mom_borsh = WebElement(
        xpath='//*[@id="right-inner"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]')

