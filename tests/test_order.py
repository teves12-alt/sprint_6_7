import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_DATA_SETS


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Заказ через верхнюю кнопку — {data[name]} {data[surname]}")
    @pytest.mark.parametrize("data", ORDER_DATA_SETS,
                             ids=["Иван_Иванов", "Анна_Смирнова"])
    def test_order_via_header_button(self, driver, data):
        main_page = MainPage(driver)
        main_page.click_cookie_button()
        main_page.click_order_button_header()
        order_page = OrderPage(driver)
        order_page.make_order(data)
        assert order_page.is_order_success_displayed(), "Окно успешного заказа не появилось"

    @allure.title("Заказ через нижнюю кнопку — {data[name]} {data[surname]}")
    @pytest.mark.parametrize("data", ORDER_DATA_SETS,
                             ids=["Иван_Иванов", "Анна_Смирнова"])
    def test_order_via_bottom_button(self, driver, data):
        main_page = MainPage(driver)
        main_page.click_cookie_button()
        main_page.click_order_button_bottom()
        order_page = OrderPage(driver)
        order_page.make_order(data)
        assert order_page.is_order_success_displayed(), "Окно успешного заказа не появилось"
