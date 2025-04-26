import allure
import pytest

from pages.home_page import HomePageScooter
from data import test_data_for_test_important_questions


class TestImportantQuestions:
    @allure.title('Проверка корректности отображения информации в разделе "Вопросы о важном"')
    @pytest.mark.parametrize("button_locator, text_locator, expected_text",
                             test_data_for_test_important_questions)
    def test_open_and_check_text(self, driver, open_home_page, button_locator, text_locator,
                                 expected_text):
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page()
        home_page.scroll_to_important_questions()
        home_page.click_cookie_button()
        home_page.wait_for_load_question(button_locator)
        home_page.click_question(button_locator)
        home_page.wait_for_load_info(text_locator)
        actual_result = home_page.get_info_text(text_locator)
        assert actual_result == expected_text, f'Ожидаемый текст: "{expected_text}", но получили: "{actual_result}".'