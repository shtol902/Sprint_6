from data import Url
from locators.logo_locators import LogoLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

class Logo(BasePage):
    @allure.step('Клик по логотипу "Яндекс"')
    def click_logo_yandex(self):
        self.click_element(LogoLocators.LOGO_YANDEX)

    @allure.step('Клик по логотипу "Самокат"')
    def check_logo_scooter_change_url_home_page(self):
        self.click_element(LogoLocators.LOGO_SCOOTER)
        return self.get_url()

    @allure.step('Открыть страницу "Самокат"')
    def open_main_page(self):
        self.open_page(Url.SCOOTER_HOMEPAGE)

    @allure.step('Проверить открытие страницы Dzen')
    def check_dzen_logo(self):
        self.find_element(LogoLocators.LOGO_DZEN)
        return self.get_url()

    @allure.step('Переход на страницу Dzen')
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

