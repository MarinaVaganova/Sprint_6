import allure

from pages.base_page import BasePage
from locators.home_page_yandex_locators import HomePageYandexLocators


class HomePageYandex(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ждём загрузки главной страницы Яндекс.Дзен')
    def wait_for_load_home_page(self):
        self.find_element(HomePageYandexLocators.NEWS_CONTENT_YANDEX)