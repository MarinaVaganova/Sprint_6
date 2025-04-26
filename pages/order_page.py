import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import URLCollection


class OrderPageScooter(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем страницу заказа самоката")
    def open_order_page(self):
        self.navigate(URLCollection.SCOOTER_ORDER_PAGE)

    @allure.step('Ждём загрузки страницы заказа')
    def wait_for_load_order_page(self):
        self.find_element(OrderPageLocators.PANEL_ORDER)

    @allure.step("Вводим имя")
    def enter_first_name(self, text):
        self.find_element(OrderPageLocators.INPUT_FIRST_NAME_FIELD).send_keys(text)

    @allure.step("Вводим фамилию")
    def enter_second_name(self, text):
        self.find_element(OrderPageLocators.INPUT_SECOND_NAME_FIELD).send_keys(text)

    @allure.step("Вводим адрес")
    def enter_address(self, text):
        self.find_element(OrderPageLocators.INPUT_ADDRESS_FIELD).send_keys(text)

    @allure.step("Вводим станцию метро")
    def enter_metro_station(self, text):
        self.find_element(OrderPageLocators.INPUT_METRO_STATION_SEARCH).send_keys(text)

    @allure.step("Выбираем станцию метро из селектора")
    def choose_metro_station(self, locator):
        self.find_element(locator).click()

    @allure.step("Вводим номер телефона")
    def enter_phone_number(self, text):
        self.find_element(OrderPageLocators.INPUT_PHONE_NUMBER_FIELD).send_keys(text)

    @allure.step('Нажимаем на кнопку "Далее"')
    def click_button_next(self):
        self.find_element(OrderPageLocators.BUTTON_NEXT).click()

    @allure.step("Вводим дату доставки")
    def enter_delivery_date(self, text):
        self.find_element(OrderPageLocators.INPUT_DELIVERY_DATE).send_keys(text)

    @allure.step("Выбираем нужную дату в календаре")
    def select_delivery_date(self, locator):
        self.find_element(locator).click()

    @allure.step('Нажимаем "Срок аренды"')
    def click_to_select_rental_period(self):
        self.find_element(OrderPageLocators.SELECT_RENTAL_PERIOD).click()

    @allure.step("Выбираем срок аренды")
    def choose_rental_period(self, locator):
        self.find_element(locator).click()

    @allure.step("Выбираем цвет самоката")
    def choose_scooter_color(self, locator):
        self.find_element(locator).click()

    @allure.step("Пишем комментарий курьеру")
    def enter_comment_for_courier(self, text):
        self.find_element(OrderPageLocators.INPUT_COMMENT_FOR_COURIER).send_keys(text)

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_make_an_order(self):
        self.find_element(OrderPageLocators.BUTTON_MAKE_AN_ORDER).click()

    @allure.step("Ждём загрузки окна подтверждения заказа")
    def wait_for_load_confirmation_order(self):
        self.find_element(OrderPageLocators.PANEL_CONFIRMATION_TO_ORDER)

    @allure.step('Нажимаем "Да" чтобы подтвердить заказ')
    def click_button_yes_to_confirm_order(self):
        self.find_element(OrderPageLocators.BUTTON_YES).click()

    @allure.step("Ждём загрузки окна об успешном заказе")
    def wait_for_load_successful_order(self):
        self.find_element(OrderPageLocators.PANEL_SUCCESSFUl_ORDER)

    @allure.step("Проверка отображения подтверждения успешного заказа")
    def successful_order_is_displayed(self):
        return self.panel_confirm_order_is_displayed(OrderPageLocators.PANEL_SUCCESSFUl_ORDER)

    @allure.step("Нажимаем на логотип 'Самокат'")
    def click_button_logo_scooter(self):
        self.find_element(OrderPageLocators.BUTTON_LOGO_SCOOTER).click()

    @allure.step("Нажимаем на логотип 'Яндекс'")
    def click_button_logo_yandex(self):
        self.find_element(OrderPageLocators.BUTTON_LOGO_YANDEX).click()