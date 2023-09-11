from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

	def add_product_to_basket(self):           # добавляем продукт в корзину
		assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Button \'add to basket\' is not presented"
		self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()

	def set_product_name(self):                # получаем название продукта
		assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
		return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

	def set_product_price(self):               # получаем цену продукта
		assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
		return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

	def set_added_product_name(self):          # получаем название добавленного в корзину продукта (из сообщения)
		assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME), "Added product name is not presented"
		return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text

	def set_added_product_price(self):          # получаем цену добавленного в корзину продукта (из сообщения)
		assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_PRICE), "Added product price is not presented"
		return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text

	def should_be_identical_names(self, name1, name2):    # сравнение наименований
		assert name1 == name2, "Product name and Added product name are different" 

	def should_be_identical_prices(self, price1, price2):    # сравнение цен
		assert price1 == price2, "Product price and Added product price are different"

	def should_not_be_success_message(self):    # проверка на то, что не должно быть сообщения об успешном добавлении товара в корзину
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

	def should_be_disappeared(self):            # проверка на то, что сообщение об успешном добавлении товара в корзину должно исчезнуть 
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be disappeared"

