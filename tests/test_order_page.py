import pytest
from data import Url, Users
from pages.order_page import OrderPage
from locators.order_locators import OrderFormLocators1, OrderFormLocators2
import allure


@allure.feature('Тесты - предзаказ самоката')
class TestOrderPage:
    @allure.title('Проверка перехода на форму заказа через кнопку "Заказать" в хедере')
    @allure.description(
        'Проверяем, что при клике на кнопку "Заказать" в хедере редиректит на форму заказа')
    def test_check_button_to_order_header(self, driver):
        driver.get(Url.SCOOTER_HOMEPAGE)
        order_page = OrderPage(driver)
        element = order_page.check_button_to_order_header()
        assert element is not None

    @allure.title('Проверка перехода на форму заказа через кнопку "Заказать" в теле главной страницы')
    @allure.description(
        'Проверяем, что при клике кнопки "Заказать" в теле главной страницы редиректит на форму заказа')
    def test_check_button_to_order_body(self, driver):
        driver.get(Url.SCOOTER_HOMEPAGE)
        order_page = OrderPage(driver)
        element = order_page.check_button_to_order_body()
        assert element is not None

    @allure.title('Проверка оформления заказа с разными данными')
    @allure.description('Проверяем, что заказы успешно оформляются с разными данными двух пользователей.')
    @pytest.mark.parametrize(
        "name, last_name, address, metro, phone, rental_day, comment_for_courier",
        [
            (Users.name_1, Users.last_name_1, Users.address_1, OrderFormLocators1.KRASNOSELSKAYA_STATION,
             Users.phone_1, OrderFormLocators2.RENT_1_DAY,
             Users.comment_for_courier_1),
            (Users.name_2, Users.last_name_2, Users.address_2, OrderFormLocators1.LUBYANKA_STATION,
             Users.phone_2, OrderFormLocators2.RENT_2_DAYS,
             Users.comment_for_courier_2)
        ],
        ids=['Оформление заказа с данными пользователя 1', 'Оформление заказа с данными пользователя 2']
    )
    def test_order_with_different_user_data(self, driver, name, last_name, address, metro, phone, rental_day, comment_for_courier):
        driver.get(Url.SCOOTER_HOMEPAGE)
        order_page = OrderPage(driver)
        order_page.check_button_to_order_header()
        order_page.add_user_data_to_form_order(name, last_name, address, metro, phone, rental_day,
                                               comment_for_courier)
        text = order_page.check_window_successful_order()
        assert 'Заказ оформлен' in text