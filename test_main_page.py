from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
	def test_guest_can_go_to_login_page(self, browser):
		#link = "http://selenium1py.pythonanywhere.com/"
		page = MainPage(browser,link)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
		page.open()                          # открываем страницу    
		page.go_to_login_page()              # выполняем метод страницы — переходим на страницу логина
		login_page = LoginPage(browser, browser.current_url)  #инициализируем страницу логина
		login_page.should_be_login_page()    # выполняем метод страницы - проверка страницы логина

	def test_guest_should_see_login_link(self, browser):
		#link = "http://selenium1py.pythonanywhere.com/"
		page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
		page.open()                    # открываем страницу
		page.should_be_login_link()    # выполняем метод страницы — проверяем что доступна ссылка на логин

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	page = BasketPage(browser, link)         # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open()                              # открываем страницу
	page.go_to_basket()                      # переход в корзину по кропке в шапке
	page.should_not_be_product_in_basket()   # проверка, что в корзине нет товара
	page.should_be_text_about_not_products_in_basket() # должен быть текст о том, что корзина пуста
