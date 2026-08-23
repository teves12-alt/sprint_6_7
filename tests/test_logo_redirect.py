import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from data import MAIN_PAGE_URL, DZEN_URL


@allure.feature("Редирект по логотипам")
class TestLogoRedirect:

    @allure.title("Клик по логотипу «Самокат» ведёт на главную")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_cookie_button()
        main_page.click_order_button_header()
        main_page.click_scooter_logo()
        assert main_page.get_current_url() == MAIN_PAGE_URL

    @allure.title("Клик по логотипу «Яндекс» ведёт на Дзен")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_cookie_button()
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        WebDriverWait(driver, 15).until(
            lambda d: "dzen.ru" in d.current_url
        )
        assert "dzen.ru" in driver.current_url
