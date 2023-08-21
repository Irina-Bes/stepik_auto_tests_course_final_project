from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('offer_nummer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer_nummer):
	#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_nummer}"
	page = ProductPage(browser,link)                # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open()                                     # открываем страницу  
	product_name = page.set_product_name()          # получаем название продукта
	product_price = page.set_product_price()        # получаем цену продукта  
	page.add_product_to_basket()                    # выполняем метод страницы — добавляем продукт в корзину
	page.solve_quiz_and_get_code()                  # посчитать результат математического выражения и ввести ответ
	added_product_name = page.set_added_product_name()    # получаем название добавленного в корзину продукта (из сообщения)
	added_product_price = page.set_added_product_price()  # получаем цену добавленного в корзину продукта (из сообщения)
	assert product_name == added_product_name, "Product name and Added product name are different" 
	assert product_price == added_product_price, "Product price and Added product price are different"



