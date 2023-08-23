from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('offer_nummer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, offer_nummer):
	#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
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
	page = MainPage(browser,link)                    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open()                                      # открываем страницу    
	page.go_to_login_page()                          # выполняем метод страницы — переходим на страницу логина
	login_page = LoginPage(browser, browser.current_url)  #инициализируем страницу логина
	login_page.should_be_login_page()                # выполняем метод страницы - проверка страницы логина