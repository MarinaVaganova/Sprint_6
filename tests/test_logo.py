import allure
import pytest

from pages.home_page_yandex import HomePageYandex
from pages.order_page import OrderPageScooter
from pages.home_page import HomePageScooter


class TestLogoNavigation:
    @allure.title('Проверка перехода на главную страницу "Самоката" при нажатии на логотип "Самокат"')
    def test_click_scooter_logo_navigates_to_home_page(self, driver, open_order_page):
        order_page = OrderPageScooter(driver)
        order_page.click_button_logo_scooter()
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page()
        actual_result = order_page.get_current_url()
        expected_result = 'https://qa-scooter.praktikum-services.ru/'
        assert actual_result == expected_result, f'Ожидаемый адрес: {actual_result}, но получили: {expected_result}'

    @allure.title('Проверка перехода на главную страницу "Дзена" при нажатии на логотип Яндекса')
    def test_click_yandex_logo_navigates_to_yandex_home_page(self, driver, open_order_page):
        order_page = OrderPageScooter(driver)
        order_page.click_button_logo_yandex()
        home_page_yandex = HomePageYandex(driver)
        home_page_yandex.switch_to_new_window()
        home_page_yandex.wait_for_load_home_page()
        actual_result = home_page_yandex.get_current_url()
        expected_result = 'https://dzen.ru/?yredirect=true'
        assert actual_result == expected_result, f'Ожидаемый адрес: {actual_result}, но получили: {expected_result}'