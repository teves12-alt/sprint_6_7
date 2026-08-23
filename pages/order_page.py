import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Заполняем первую форму: имя, фамилия, адрес, метро, телефон')
    def fill_first_form(self, name, lastname, address, metro, phone):
        self.set_text(OrderPageLocators.NAME_INPUT, name)
        self.set_text(OrderPageLocators.LASTNAME_INPUT, lastname)
        self.set_text(OrderPageLocators.ADDRESS_INPUT, address)
        self.set_text(OrderPageLocators.METRO_INPUT, metro)
        self.click(OrderPageLocators.metro_option(metro))
        self.set_text(OrderPageLocators.PHONE_INPUT, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем вторую форму: дата, срок, цвет, комментарий')
    def fill_second_form(self, date, rent_period, color_locator, comment):
        self.set_text(OrderPageLocators.DATE_INPUT, date)
        self.click(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.rent_period_option(rent_period))
        self.click(color_locator)
        self.set_text(OrderPageLocators.COMMENT_INPUT, comment)
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.YES_BUTTON)

    @allure.step('Полный флоу заказа: заполнение обеих форм и подтверждение')
    def make_order(self, name, lastname, address, metro, phone, date, rent_period, color_locator, comment):
        self.fill_first_form(name, lastname, address, metro, phone)
        self.fill_second_form(date, rent_period, color_locator, comment)

    @allure.step('Проверяем, что появилось окно успешного заказа')
    def is_order_success_displayed(self):
        return self.is_element_displayed(OrderPageLocators.SUCCESS_HEADER)

    @allure.step('Получаем заголовок окна успешного заказа')
    def get_success_header_text(self):
        return self.get_text(OrderPageLocators.SUCCESS_HEADER)
