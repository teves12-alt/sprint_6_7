import allure
import pytest
from pages.main_page import MainPage
from data import FAQ_ITEMS


@allure.feature("Вопросы о важном")
class TestQuestions:

    @allure.title("Раскрытие ответа на вопрос: {question}")
    @pytest.mark.parametrize("index, question, expected_answer", FAQ_ITEMS,
                             ids=[f"question_{i}" for i in range(len(FAQ_ITEMS))])
    def test_question_opens_correct_answer(self, driver, index, question, expected_answer):
        main_page = MainPage(driver)
        main_page.click_cookie_button()
        main_page.click_question_arrow(index)
        assert main_page.is_answer_visible(index), f"Ответ на вопрос {index} не раскрылся"
        actual = main_page.get_answer_text(index)
        assert expected_answer in actual, (
            f"Ожидаемый текст: {expected_answer!r}, фактический: {actual!r}"
        )
