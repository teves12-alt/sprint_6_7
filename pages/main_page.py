import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Кликаем по кнопке «Заказать» вверху страницы')
    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step('Кликаем по кнопке «Заказать» внизу страницы')
    def click_order_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('Кликаем по логотипу «Самокат»')
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOUTER_LOGO)

    @allure.step('Кликаем по логотипу «Яндекс»')
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    @allure.step('Кликаем по кнопке согласия с куки')
    def click_cookie_button(self):
        self.click(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Раскрываем вопрос №{index} в аккордеоне')
    def click_question_arrow(self, index):
        self.scroll_to_element(MainPageLocators.question_arrow(index))
        self.click(MainPageLocators.question_arrow(index))

    @allure.step('Получаем текст ответа на вопрос №{index}')
    def get_question_answer_text(self, index):
        return self.get_text(MainPageLocators.question_answer(index))

    @allure.step('Проверяем, что ответ на вопрос №{index} виден')
    def is_answer_displayed(self, index):
        return self.is_element_displayed(MainPageLocators.question_answer(index))
