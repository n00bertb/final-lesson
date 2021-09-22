from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time
import pytest

@pytest.mark.reg_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        email = str(time.time()) + "@fakemail.org"
        print(email)
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()
        page.register_new_user(email,"PasswordBigBrain")
        #time.sleep(100)
        page.should_be_authorized_user()
        #time.sleep(100)
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.add_to_basket()    #жмем кнопку добавить в карзину
        page.solve_quiz_and_get_code() #решаем задачу и получаем ответ
        page.should_be_same_product_name() #проверяем что добавился верный продукт в корзину
        page.should_be_correct_basket_price() #проверяем что цена в корзине коректная

    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
 
@pytest.mark.need_review       
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link =  f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_basket()    #жмем кнопку добавить в карзину
    page.solve_quiz_and_get_code() #решаем задачу и получаем ответ
    #time.sleep(10)
    page.should_be_same_product_name() #проверяем что добавился верный продукт в корзину
    page.should_be_correct_basket_price() #проверяем что цена в корзине коректная

@pytest.mark.need_review      
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_basket_page()        # переходим в корзину
    page.check_emty_basket()        #проверяем корзину на пустоту
    #time.sleep(1000)
