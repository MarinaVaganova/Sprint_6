from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators


class URLCollection:
    SCOOTER_HOME_PAGE = 'https://qa-scooter.praktikum-services.ru/'
    YANDEX_HOME_PAGE = 'https://dzen.ru/?yredirect=true'
    SCOOTER_ORDER_PAGE = 'https://qa-scooter.praktikum-services.ru/order'


test_data_for_test_important_questions = [
    (HomePageLocators.BUTTON_COST_AND_PAYMENT, HomePageLocators.TEXT_COST_AND_PAYMENT_INFO,
     'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
    (HomePageLocators.BUTTON_MULTIPLE_SCOOTERS, HomePageLocators.TEXT_MULTIPLE_SCOOTERS_INFO,
     'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
     'можете просто сделать несколько заказов — один за другим.'),
    (HomePageLocators.BUTTON_RENTAL_TIME_CALCULATION, HomePageLocators.TEXT_RENTAL_TIME_CALCULATION_INFO,
     'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды '
     'начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, '
     'суточная аренда закончится 9 мая в 20:30.'),
    (HomePageLocators.BUTTON_ORDER_TODAY, HomePageLocators.TEXT_ORDER_TODAY_INFO,
     'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
    (HomePageLocators.BUTTON_EXTEND_OR_EARLY_RETURN, HomePageLocators.TEXT_EXTEND_OR_EARLY_RETURN_INFO,
     'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
    (HomePageLocators.BUTTON_CHARGER_INCLUDED, HomePageLocators.TEXT_CHARGER_INCLUDED_INFO,
     'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без '
     'передышек и во сне. Зарядка не понадобится.'),
    (HomePageLocators.BUTTON_CANCEL_ORDER, HomePageLocators.TEXT_CANCEL_ORDER_INFO,
     'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
    (HomePageLocators.BUTTON_DELIVERY_BEYOND_MKAD, HomePageLocators.TEXT_DELIVERY_BEYOND_INFO,
     'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
]

order_data = [
    {
        'first_name': 'Марина',
        'second_name': 'Ваганова',
        'address': 'Пенза',
        'metro_station': 'Университет',
        'metro_selection': OrderPageLocators.BUTTON_STATE_1,
        'phone_number': '+79273702508',
        'delivery_date': '05.05.2025',
        'date_selection': OrderPageLocators.SELECT_05_05_25,
        'rental_period': OrderPageLocators.OPTION_RENTAL_PERIOD_ONE_DAY,
        'scooter_color': OrderPageLocators.CHECKBOX_BLACK_COLOR,
        'courier_comment': 'Тест',
        'location': 'top'
    },
    {
        'first_name': 'Марина',
        'second_name': 'Ваганова',
        'address': 'Пенза',
        'metro_station': 'ВДНХ',
        'metro_selection': OrderPageLocators.BUTTON_STATE_2,
        'phone_number': '+79273902509',
        'delivery_date': '10.05.2025',
        'date_selection': OrderPageLocators.SELECT_10_05_25,
        'rental_period': OrderPageLocators.OPTION_RENTAL_PERIOD_THREE_DAY,
        'scooter_color': OrderPageLocators.CHECKBOX_GREY_COLOR,
        'courier_comment': 'Тест',
        'location': 'bottom'
    }
]