from selenium.webdriver.common.by import By

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")

class BasketPageLocators():
	BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
	NOT_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner p")

#class MainPageLocators():


class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
	ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
	ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner p strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")