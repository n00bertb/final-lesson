from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def check_emty_basket(self):
        self.should_be_emty_basket_text()
        self.should_be_no_products_in_basket()
        
    def add_to_basket(self):
        basket_button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        basket_button.click()
        
    def should_be_emty_basket_text(self):
        emty_text='Your basket is empty. Continue shopping'
        assert emty_text == self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text, "Text not presented, basket not empty"
    
    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_BUTTON), "Product is presented in basket, but should not be"