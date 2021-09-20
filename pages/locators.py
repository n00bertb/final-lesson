from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON = (By.NAME, "registration_submit")
    
class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_ADD = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BASKET_PRICE_CORRECT = (By.CSS_SELECTOR, ".alert-info strong")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR,".alert-success")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    