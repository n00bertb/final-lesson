from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Not login url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
          
    def register_new_user(self,email, password):
        login=self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        login.send_keys(email)
        pass1=self.browser.find_element(*LoginPageLocators.PASSWORD1)
        pass1.send_keys(password)
        pass2=self.browser.find_element(*LoginPageLocators.PASSWORD2)
        pass2.send_keys(password)
        button=self.browser.find_element(*LoginPageLocators.BUTTON)
        button.click()