import pytest
from pages.base_page import BasePage
from locators.order_locators import OrderButtonLocators, OrderFormLocators1, OrderFormLocators2, OrderWindowLocators, CookieButton
from data import Users
import allure


class OrderPage(BasePage):

    @allure.step('Перейти на форму заказа по кнопке "Заказать" в хедере')
    def check_button_to_order_header(self):
        self.click_element(OrderButtonLocators.BUTTON_TO_ORDER_HEADER)
        return self.find_element(OrderFormLocators1.INPUT_NAME)

    @allure.step('Перейти на форму заказа по кнопке "Заказать" в теле страницы')
    def check_button_to_order_body(self):
        self.scroll_to_element(OrderButtonLocators.BUTTON_TO_ORDER_BODY)
        self.click_element(OrderButtonLocators.BUTTON_TO_ORDER_BODY)
        return self.find_element(OrderFormLocators1.INPUT_NAME)

    @allure.step('Заполнить форму заказа')
    def add_user_data_to_form_order(self, name, last_name, address, metro, phone, rental_day,
                                    comment_for_courier):
        self.click_element(CookieButton.ACCEPT_COOKIE)
        self.add_text_to_element(OrderFormLocators1.INPUT_NAME, name)
        self.add_text_to_element(OrderFormLocators1.INPUT_LAST_NAME, last_name)
        self.add_text_to_element(OrderFormLocators1.INPUT_ADDRESS, address)
        self.click_element(OrderFormLocators1.INPUT_METRO_STATION)
        self.click_element(metro)
        self.add_text_to_element(OrderFormLocators1.INPUT_PHONE, phone)
        self.click_element(OrderFormLocators1.BUTTON_NEXT)
        self.click_element(OrderFormLocators2.INPUT_DATA_ORDER)
        self.click_element(OrderFormLocators2.DELIVERY_DATE_TOMORROW)
        self.click_element(OrderFormLocators2.INPUT_RENTAL_PERIOD)
        self.click_element(rental_day)
        self.click_element(OrderFormLocators2.CHECKBOX_BLACK_COLOR)
        self.add_text_to_element(OrderFormLocators2.INPUT_COMMENT_FOR_COURIER, comment_for_courier)
        self.click_element(OrderFormLocators2.BUTTON_TO_ORDER_IN_FORM)
        return self.find_element(OrderWindowLocators.BUTTON_YES_ORDER)

    @allure.step('Завершить заказ, получить поп-ап об успешном оформлении заказа')
    def check_window_successful_order(self):
        self.click_element(OrderWindowLocators.BUTTON_YES_ORDER)
        return self.get_text_from_element(OrderWindowLocators.POP_UP_WINDOW_SUCCESSFUL_ORDER)