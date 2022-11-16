# FINAL-TEST-TASK-28-PJ-04

Финальный проект по курсу Тестировщик-автоматизатор на Python (QAP).
Проект с использованием PyTest и Selenium интернет-магазина https://www.labirint.ru/. 
Тесты запускаются в браузере Chrome.
Для запуска тестов необходимо предварительно установить следующие библиотеки, список находится в файле requirements
(pip3 install -r requirements):

pytest;

pytest-selenium;

selenium;

termcolor;

allure-python-commons;

Как запускать тесты:

Скачать Selenium WebDriver с https://chromedriver.chromium.org/downloads (выбрать версию, совместимую с браузером) и скопировать в папку .chromedriver.

В команде запуска тестов необходимо указать свой путь для драйвера, в моем случае он лежит в папке C:\chromedriver\chromedriver.exe

ПАПКА tests

Запуск тестов из Terminal:

Перейти в папку с тестом - ввести: cd tests

Тестовые сценарии:

test_auth_page.py - Тестируем возможность входа в личный кабинет. 4 теста. -команда запуска:                                                                           
python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe test_auth_page.py

test_book_page.py - Тестируем книги с главной страницы. 4 теста. -команда запуска:                                                                                   
python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe test_book_page.py

test_labirint.py  - Тестируем главную страницу 44 теста. -команда запуска:                                                                                             
python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe test_labirint.py

test_search_page.py - Тестируем поиск по тексту с главной страницы. 6 тестов. -команда запуска:                                                                       
python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe test_search_page.py

test_cart_page.py - Тестируем корзину с книгами. 3 теста. -команда запуска:                                                                             
python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe test_cart_page.py

ПАПКА test_param

Запуск тестов из Terminal:

Перейти в папку с тестом - ввести: cd test_param

Тестовые сценарии:

test_parametr_home_page.py - параметризованный обход кнопок в шапке главной страницы сайта. 18 тестов. -команда запуска:                                  
python -m pytest -v --driver Chrome --driver-path test_param\chrome\chromedriver.exe test_parametr_home_page.py

test_parametr_office.py - параметризованный обход кнопок в разделе Канцтовары. 10 тестов.  -команда запуска:                                           
python -m pytest -v --driver Chrome --driver-path test_param\chrome\chromedriver.exe test_parametr_office.py
