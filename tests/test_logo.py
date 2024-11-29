from pages.logo_page import Logo
from data import Url
import time
import allure


@allure.feature('Тесты - клик по логотипам')
class TestLogoRedirect:

    @allure.title('Переход на Дзен по клику на логотип "Яндекс"')
    @allure.description('Находим логотип "Яндекс" и проверяем, что по клику на него происходит переход на новую страницу Дзен')
    def test_open_new_window_dzen(self, driver):
        logo = Logo(driver)
        logo.open_main_page()
        logo.click_logo_yandex()
        logo.switch_to_new_window()
        time.sleep(5)
        dzen_url = logo.check_dzen_logo()
        assert Url.DZEN_HOMEPAGE in dzen_url

    @allure.title('Переход на главную страницу "ЯндексСамокат" по клику на логотип "Самокат"')
    @allure.description(
        'Находим логотип "Самокат" и проверяем, что по клику на него происходит переход на главную страницу "ЯндексСамокат"')
    def test_check_logo_scooter_change_url_home_page(self, driver):
        logo = Logo(driver)
        logo.open_main_page()
        new_url = logo.check_logo_scooter_change_url_home_page()
        assert new_url == Url.SCOOTER_HOMEPAGE