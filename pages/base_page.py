from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def scroll_into_view(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView()", locator)

    def wait_for_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator, timeout=10):
        self.find_element(locator, timeout).click()

    def enter_text1(self, locator, text, timeout=10):
        self.find_element(locator, timeout).send_keys(text)

    def panel_confirm_order_is_displayed(self, locator):
        panel_confirm_order = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return panel_confirm_order.is_displayed()

    def switch_to_new_window(self):
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            self.driver.switch_to.window(window_handles[1])
        else:
            raise Exception("Нет дополнительного окна для переключения")