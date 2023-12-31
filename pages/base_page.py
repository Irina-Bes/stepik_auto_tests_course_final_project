from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators

import math

class BasePage():

	def __init__(self, browser, url, timeout=10):      # обозначаем текущую страницу, url и ожидание
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)

	def open(self):                                    # открытие страницы
		self.browser.get(self.url)

# переходы на страницы

	def go_to_login_page(self):                        # переход на страницу логина
		link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
		link.click()

	def go_to_basket(self):                            # переход в корзину по кнопке в шапке
		basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
		basket_link.click()

# проверки наличия элементов

	def should_be_login_link(self):                    # проверка наличия ссылки на страницу логина
		assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

	def is_element_present(self, how, what):           # проверка что элемент есть на странице
		try:
			self.browser.find_element(how, what)
		except (NoSuchElementException):
			return False
		return True

# проверки отcутствия элементов

	def is_not_element_present(self, how, what, timeout=4):  # проверка что элемента нет на странице (ждем 4 сек)
		try:
			WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return True
		return False

	def is_disappeared(self, how, what, timeout=4):          # проверка что элемент исчез со страницы (ждем 4 сек)
		try:
			WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return False
		return True

# прочие проверки

	def should_be_authorized_user(self):                     # проверка что пользователь авторизован
		assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"

# вспомогательные функции

	def solve_quiz_and_get_code(self):                       # формула расчета квиза
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.browser.switch_to.alert
			alert_text = alert.text
			print(f"Your code: {alert_text}")
			alert.accept()
		except NoAlertPresentException:
			print("No second alert presented")