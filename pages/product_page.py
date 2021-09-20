from .base_page import BasePage
from .locators import BasketPageLocators

class ProductPage(BasePage):
    def should_be_add(self):
        self.should_be_same_product_name()
        #self.should_be_correct_basket_price()
        
    def add_to_basket(self):
        basket_button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        basket_button.click()
        
    def should_be_same_product_name(self):
        product_name=self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text
        #product_name="wrong"+product_name     
        print(product_name)
        product_name1=self.browser.find_element(*BasketPageLocators.PRODUCT_NAME_ADD).text
        print(product_name1)
        #assert product_name == self.browser.find_element(*BasketPageLocators.PRODUCT_NAME_ADD).text, "Product name not correct"
        assert product_name == product_name1, "Product name not correct"
        
    def should_be_correct_basket_price(self):
        product_price=self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text
        #product_price="wrong"+product_price
        print(product_price)
        product_price1=self.browser.find_element(*BasketPageLocators.BASKET_PRICE_CORRECT).text
        print(product_price1)
        #assert product_price == self.browser.find_element(*BasketPageLocators.BASKET_PRICE_CORRECT).text, "Price in basket is not correct"
        assert product_price == product_price1, "Price in basket is not correct"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*BasketPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"