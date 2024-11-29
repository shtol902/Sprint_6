from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(text)

    def get_text_from_element(self, locator):
        element = self.find_element(locator)
        return element.text

    def format_to_locator(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_url(self):
        return self.driver.current_url

    def open_page(self, url):
        self.driver.get(url)

