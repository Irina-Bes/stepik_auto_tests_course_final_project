from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):             # проверки корректности страницы логина
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):              # текущий url содержит 'Login'
        assert "login" in self.browser.current_url, "\'Login\' not in current url"

    def should_be_login_form(self):             # на странице есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):          # на странице есть форма регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):     # регистарция пользователя
        self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Input for REGISTRATION_EMAIL is not presented"
        self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Input for REGISTRATION_PASSWORD1 is not presented"
        self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Input for REGISTRATION_PASSWORD2 is not presented"
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2).send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_BUTTON), "REGISTER_FORM_BUTTON is not presented, but should be"
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON).click()
        assert self.is_element_present(*LoginPageLocators.SUCCESSFUL_REGISTRATION_MESSAGE), "Success registration message is not presented, but should be"
