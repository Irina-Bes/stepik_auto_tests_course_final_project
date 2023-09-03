from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
import time

@pytest.mark.parametrize('offer_nummer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, offer_nummer):
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_nummer}"
	page = ProductPage(browser,link)                # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open()                                     # открываем страницу  
	product_name = page.set_product_name()          # получаем название продукта
	product_price = page.set_product_price()        # получаем цену продукта  
	page.add_product_to_basket()                    # добавляем продукт в корзину
	page.solve_quiz_and_get_code()                  # посчитать результат математического выражения и ввести ответ
	added_product_name = page.set_added_product_name()    # получаем название добавленного в корзину продукта (из сообщения)
	added_product_price = page.set_added_product_price()  # получаем цену добавленного в корзину продукта (из сообщения)
	assert product_name == added_product_name, "Product name and Added product name are different" 
	assert product_price == added_product_price, "Product price and Added product price are different"

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser,link)                # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open()                                     # открываем страницу  
	page.add_product_to_basket()                    # добавляем продукт в корзину
	page.should_not_be_success_message()            # проверка на то, что не должно быть сообщения об успешном добавлении товара в корзину

def test_guest_cant_see_success_message(browser): 
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser,link)                # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open()                                     # открываем страницу
	page.should_not_be_success_message()            # проверка на то, что не должно быть сообщения об успешном добавлении товара в корзину

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser,link)                # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open()                                     # открываем страницу
	page.add_product_to_basket()                    # добавляем продукт в корзину
	page.should_be_disappeared()                    # проверка на то, что сообщение об успешном добавлении товара в корзину должно исчезнуть

def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)               # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open()                                     # открываем страницу
	page.should_be_login_link()                     # проверяем что есть ссылка перехода на логин

def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = MainPage(browser,link)                         # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open()                                           # открываем страницу
	page.go_to_login_page()                               # выполняем метод страницы — переходим на страницу логина
	login_page = LoginPage(browser, browser.current_url)  # инициализируем страницу логина
	login_page.should_be_login_page()                     # выполняем метод страницы - проверка страницы логина

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = BasketPage(browser,link)                      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open()                                          # открываем страницу
	page.go_to_basket()                                  # переход в корзину по кропке в шапке
	page.should_not_be_product_in_basket()               # проверка, что в корзине нет товара
	page.should_be_text_about_not_products_in_basket()   # должен быть текст о том, что корзина пуста


@pytest.mark.user_on_product_page
class TestUserAddToBasketFromProductPage():

	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		page = LoginPage(browser,link)                  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
		page.open()                                     # открываем страницу
		page.go_to_login_page()                         # переходим на страницу логина
		email = str(time.time()) + "@fakemail.org"
		password = str(time.time()) + "fakepassword"
		page.register_new_user(email, password)         # регистрируем пользователя
		page.should_be_authorized_user()                # проверяем что пользователь зарегестрирован

	def test_user_cant_see_success_message(self, browser): 
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		page = ProductPage(browser,link)                # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
		page.open()                                     # открываем страницу
		page.should_not_be_success_message()            # проверка на то, что не должно быть сообщения об успешном добавлении товара в корзину

	def test_user_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
		page = ProductPage(browser,link)                      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
		page.open()                                           # открываем страницу  
		product_name = page.set_product_name()                # получаем название продукта
		product_price = page.set_product_price()              # получаем цену продукта  
		page.add_product_to_basket()                          # добавляем продукт в корзину
		page.solve_quiz_and_get_code()                        # посчитать результат математического выражения и ввести ответ
		added_product_name = page.set_added_product_name()    # получаем название добавленного в корзину продукта (из сообщения)
		added_product_price = page.set_added_product_price()  # получаем цену добавленного в корзину продукта (из сообщения)
		assert product_name == added_product_name, "Product name and Added product name are different" 
		assert product_price == added_product_price, "Product price and Added product price are different"
