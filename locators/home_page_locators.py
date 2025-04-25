from selenium.webdriver.common.by import By


class HomePageLocators:
    PANEL_HOME_FIRST_PART = [By.CLASS_NAME, 'Home_FirstPart__3g6vG']
    BUTTON_ORDER_ON_HEADER = [By.XPATH, './/button[@class="Button_Button__ra12g"]']
    BUTTON_ORDER_ON_BOTTOM = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']
    PANEL_IMPORTANT_QUESTIONS = [By.CLASS_NAME, 'Home_FourPart__1uthg']
    COOKIE_BUTTON_LOCATOR = [By.ID, "rcc-confirm-button"]

    BUTTON_COST_AND_PAYMENT = [By.XPATH, './/div[@id="accordion__heading-0"]']
    TEXT_COST_AND_PAYMENT_INFO = [By.XPATH, ".//div[@id='accordion__panel-0']"]

    BUTTON_MULTIPLE_SCOOTERS = [By.XPATH, './/div[@id="accordion__heading-1"]']
    TEXT_MULTIPLE_SCOOTERS_INFO = [By.XPATH, ".//div[@id='accordion__panel-1']"]

    BUTTON_RENTAL_TIME_CALCULATION = [By.XPATH, './/div[@id="accordion__heading-2"]']
    TEXT_RENTAL_TIME_CALCULATION_INFO = [By.XPATH, ".//div[@id='accordion__panel-2']"]

    BUTTON_ORDER_TODAY = [By.XPATH, './/div[@id="accordion__heading-3"]']
    TEXT_ORDER_TODAY_INFO = [By.XPATH, ".//div[@id='accordion__panel-3']"]

    BUTTON_EXTEND_OR_EARLY_RETURN = [By.XPATH, './/div[@id="accordion__heading-4"]']
    TEXT_EXTEND_OR_EARLY_RETURN_INFO = [By.XPATH, ".//div[@id='accordion__panel-4']"]

    BUTTON_CHARGER_INCLUDED = [By.XPATH, './/div[@id="accordion__heading-5"]']
    TEXT_CHARGER_INCLUDED_INFO = [By.XPATH, ".//div[@id='accordion__panel-5']"]

    BUTTON_CANCEL_ORDER = [By.XPATH, './/div[@id="accordion__heading-6"]']
    TEXT_CANCEL_ORDER_INFO = [By.XPATH, ".//div[@id='accordion__panel-6']"]

    BUTTON_DELIVERY_BEYOND_MKAD = [By.XPATH, './/div[@id="accordion__heading-7"]']
    TEXT_DELIVERY_BEYOND_INFO = [By.XPATH, ".//div[@id='accordion__panel-7']"]