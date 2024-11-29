from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class HomePage(BasePage):
    @allure.step('Получаем текст вопросов')
    def check_question_text(self, num):
        locator_question_formatted = self.format_to_locator(MainPageLocators.LOCATOR_QUESTION, num)
        self.scroll_to_element(MainPageLocators.SUB_HEADER)
        self.find_element(locator_question_formatted)
        return self.get_text_from_element(locator_question_formatted)

    @allure.step('Получаем текст ответов')
    def check_answer_text(self, num):
        locator_question_formatted = self.format_to_locator(MainPageLocators.LOCATOR_QUESTION, num)
        locator_answer_formatted = self.format_to_locator(MainPageLocators.LOCATOR_ANSWER, num)
        self.scroll_to_element(MainPageLocators.SUB_HEADER)
        self.click_element(locator_question_formatted)
        return self.get_text_from_element(locator_answer_formatted)