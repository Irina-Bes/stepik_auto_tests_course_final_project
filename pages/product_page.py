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


