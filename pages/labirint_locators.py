import os
from pages.base import WebPage
from pages.elementes import WebElement
from pages.elementes import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    """Параметризация"""
    parametr_page = WebElement(xpath=input)

    """Авторизация"""
    my_labirint = WebElement(xpath='//a[@class="b-header-b-personal-e-link top-link-main top-link-main_cabinet  js-b-autofade-wrap"]')
    login_field = WebElement(xpath='//input[@class="full-input__input formvalidate-error"]')
    enter_button = WebElement(xpath='//input[@class="new-auth__button js-submit js-submit-by-code new-auth__input full-input__input new-forms__input_size_m"]')
    check_code_and_enter_button = WebElement(xpath='//*[@id="auth-email-sent"]/input[5]')
    auth_error = WebElement(xpath='//small[@class="full-input__msg-small js-msg-small"][text()="Введенного кода не существует"]')
    auth_error_2 = WebElement(xpath='//small[@class="full-input__msg-small js-msg-small"][text()="Нельзя использовать символ « »"]')
    page_title_cabinet = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[1]/div[1]/span[1]')

    """Результаты поиска"""
    search = WebElement(id='search-field')
    search_btn = WebElement(xpath='//button[@type="submit"]')
    successful_search = WebElement(xpath='//div[@class="index-top-title-outer"]')
    not_successful_search = WebElement(xpath='//h1[contains(text(),"Мы ничего не нашли по вашему запросу! Что делать?")]')
    all_filers_button = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[4]/span/span/span/span')
    reset_all_filers = WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[1]/div/div[2]/div/span[3]')
    available = WebElement(xpath='//*[@id="section-search-form"]/div[2]/div[2]/div[1]/label[1]')
    show_all_found_button = WebElement(xpath='//input[@class="show-goods__button"]')
    available_products_titles = ManyWebElements(xpath='//span[@class="product-title"]')

    """Книги"""
    best_sale = WebElement(xpath='//a[@href="/best/sale/"]')
    random_book = WebElement(xpath='//*[@class="b-productblock-e-cover"]')
    random_book_1 = WebElement(xpath='//*[@class="relative product-cover__relative"]')
    buy_book = WebElement(xpath='//*[@class="btn btn-small btn-primary btn-buy"]')
    successfuly_odered = WebElement(xpath='//span[contains(text(),"Ваш заказ")]')
    add_to_deferred = WebElement(xpath='//a[@class="fave"]')

    """Корзина"""
    cart = WebElement(xpath='//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')
    title_my_shopping_cart = WebElement(xpath='//li[@class="ui-state-default ui-corner-top ui-last-child ui-tabs-active ui-state-active"]')
    plus_one_more = WebElement(xpath='//span[@class="btn btn-increase btn-increase-cart"]')
    counter_selected_book = WebElement(xpath='//span[@id="basket-default-prod-count2"] ')
    remove_from_cart = WebElement(xpath='//a[@class ="b-link-popup"]')
    empty_cart = WebElement(xpath='//span[@class="g-alttext-small g-alttext-grey g-alttext-head"][text()="Ваша корзина пуста. Почему?"]')

    """Отложено"""
    deferred = WebElement(xpath='//span[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-putorder b-header-e-sprite-background"]')
    deferred_items = WebElement(xpath='//li[@class="cabinet-menu__tab cabinet-menu__tab_active"]')
    products_deferred = ManyWebElements(xpath='//span[@class ="product-title"]')

    """Добавить к сравнению"""
    add_to_compare_button = WebElement(xpath='//a[@class="compare big-compare"]')
    compare_button = WebElement(xpath='//a[@class="compare big-compare done"]')
    title_product_compare = WebElement(xpath='//h1[@class="compare-title"]')
    logo_labirint = WebElement(xpath='//span[@class="b-header-b-logo-e-logo"]')