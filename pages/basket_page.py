from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

	def should_not_be_product_in_basket(self):                       # проверка, что в корзине нет товара
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Product in basket, but should not be"

	def should_be_text_about_not_products_in_basket(self):           # должен быть текст о том, что корзина пуста
		assert self.is_element_present(*BasketPageLocators.NOT_PRODUCT_IN_BASKET), "Should be text about not products in basket, but text is not"